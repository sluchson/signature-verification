import csv
import json
import random
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import DataLoader

from src.dataset import SignaturePairs, ResampledPairs
from src.model import SignatureNet, contrastive_loss
from src.metrics import eer, far_frr

ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "models"
RESULTS_FILE = ROOT / "results" / "experiments.csv"

DEFAULTS = {
    "resample": True,
    "epochs": 30,
    "batch_size": 32,
    "lr": 1e-3,
    "weight_decay": 1e-4,
    "margin": 1.0,
    "dropout": 0.3,
    "embedding_dim": 128,
}

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

_datasets = {}


def get_dataset(key, factory):
    if key not in _datasets:
        _datasets[key] = factory()
    return _datasets[key]


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def train_one_epoch(model, loader, optimizer, margin):
    model.train()
    total = 0.0
    for a, b, y in loader:
        a, b, y = a.to(DEVICE), b.to(DEVICE), y.to(DEVICE)
        optimizer.zero_grad()
        loss = contrastive_loss(model(a, b), y, margin)
        loss.backward()
        optimizer.step()
        total += loss.item() * len(y)
    return total / len(loader.dataset)


@torch.no_grad()
def scores(model, dataset, batch_size=64):
    model.eval()
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    distances, labels = [], []
    for a, b, y in loader:
        distances.append(model(a.to(DEVICE), b.to(DEVICE)).cpu())
        labels.append(y)
    s = -torch.cat(distances).numpy()
    lab = torch.cat(labels).numpy()
    return s[lab == 1], s[lab == 0]


def run_experiment(name, seed, **overrides):
    config = {**DEFAULTS, **overrides}
    set_seed(seed)

    if config["resample"]:
        train_set = get_dataset("train_resampled", lambda: ResampledPairs("train"))
    else:
        train_set = get_dataset("train_fixed", lambda: SignaturePairs("train"))
    val_all = get_dataset("val_all", lambda: SignaturePairs("val"))
    val_skilled = get_dataset("val_skilled", lambda: SignaturePairs("val", ("genuine", "skilled")))
    test_skilled = get_dataset("test_skilled", lambda: SignaturePairs("test", ("genuine", "skilled")))
    test_random = get_dataset("test_random", lambda: SignaturePairs("test", ("genuine", "random")))

    train_loader = DataLoader(train_set, batch_size=config["batch_size"], shuffle=True)
    model = SignatureNet(config["embedding_dim"], config["dropout"]).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=config["lr"], weight_decay=config["weight_decay"])

    MODELS_DIR.mkdir(exist_ok=True)
    model_path = MODELS_DIR / f"{name}_seed{seed}.pt"
    history = {"train_loss": [], "val_eer": []}
    best_eer, best_epoch = 1.0, 0

    for epoch in range(1, config["epochs"] + 1):
        if config["resample"]:
            train_set.resample(seed * 1000 + epoch)
        train_loss = train_one_epoch(model, train_loader, optimizer, config["margin"])
        val_eer, _ = eer(*scores(model, val_all))
        history["train_loss"].append(train_loss)
        history["val_eer"].append(val_eer)
        if val_eer < best_eer:
            best_eer, best_epoch = val_eer, epoch
            torch.save(model.state_dict(), model_path)

    model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    _, threshold = eer(*scores(model, val_skilled))

    result = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "nazwa": name,
        "seed": seed,
        "najlepsza_epoka": best_epoch,
        "eer_walidacja": round(best_eer, 4),
    }
    for label, dataset in [("wykwalifikowane", test_skilled), ("losowe", test_random)]:
        pos, neg = scores(model, dataset)
        test_eer, _ = eer(pos, neg)
        far, frr = far_frr(pos, neg, threshold)
        result[f"eer_{label}"] = round(test_eer, 4)
        result[f"far_{label}"] = round(far, 4)
        result[f"frr_{label}"] = round(frr, 4)
    result["konfiguracja"] = json.dumps(config)

    RESULTS_FILE.parent.mkdir(exist_ok=True)
    new_file = not RESULTS_FILE.exists()
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(result.keys()))
        if new_file:
            writer.writeheader()
        writer.writerow(result)

    print(f"{name}, seed {seed}: najlepsza epoka {best_epoch}, EER test: "
          f"wykwalifikowane {result['eer_wykwalifikowane']:.1%}, losowe {result['eer_losowe']:.1%}")
    return result, history