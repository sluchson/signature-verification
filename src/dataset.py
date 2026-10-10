import csv
import itertools
import json
import random
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset
from torchvision.transforms import v2

from src.preprocessing import preprocess

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
SIGNATURES_DIR = DATA_DIR / "signatures"

PAIR_FILES = {
    "genuine": "genuine_pairs.csv",
    "skilled": "skilled_forgery_pairs.csv",
    "random": "random_forgery_pairs.csv",
}


def image_path(file_name):
    folder = "full_org" if file_name.startswith("original") else "full_forg"
    return SIGNATURES_DIR / folder / file_name


def to_tensor(img):
    return torch.from_numpy(1.0 - img.astype(np.float32) / 255.0).unsqueeze(0)


def load_image(file_name, **prep):
    return to_tensor(preprocess(image_path(file_name), **prep))


class SignaturePairs(Dataset):
    transform = None

    def __init__(self, split, pair_types=("genuine", "skilled", "random"), **prep):
        self.pairs = []
        for pair_type in pair_types:
            with open(DATA_DIR / PAIR_FILES[pair_type]) as f:
                for row in csv.DictReader(f):
                    if row["split"] == split:
                        label = 1.0 if pair_type == "genuine" else 0.0
                        self.pairs.append((row["file_a"], row["file_b"], label))

        self.images = {}
        for file_a, file_b, _ in self.pairs:
            for name in (file_a, file_b):
                if name not in self.images:
                    self.images[name] = load_image(name, **prep)

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, index):
        file_a, file_b, label = self.pairs[index]
        a, b = self.images[file_a], self.images[file_b]
        if self.transform is not None:
            a, b = self.transform(a), self.transform(b)
        return a, b, torch.tensor(label)


def files_of(writer, kind):
    return [f"{kind}_{writer}_{i}.png" for i in range(1, 25)]


class ResampledPairs(SignaturePairs):
    def __init__(self, split, genuine_per_writer=48, skilled_per_writer=24, random_per_writer=24, **prep):
        with open(DATA_DIR / "writer_split.json") as f:
            self.writers = json.load(f)[split]
        self.counts = (genuine_per_writer, skilled_per_writer, random_per_writer)
        self.images = {}
        for writer in self.writers:
            for name in files_of(writer, "original") + files_of(writer, "forgeries"):
                self.images[name] = load_image(name, **prep)
        self.resample(0)

    def resample(self, seed):
        rng = random.Random(seed)
        n_genuine, n_skilled, n_random = self.counts
        pairs = []
        for writer in self.writers:
            originals = files_of(writer, "original")
            forgeries = files_of(writer, "forgeries")
            others = [w for w in self.writers if w != writer]
            for a, b in rng.sample(list(itertools.combinations(originals, 2)), n_genuine):
                pairs.append((a, b, 1.0))
            for a, b in rng.sample(list(itertools.product(originals, forgeries)), n_skilled):
                pairs.append((a, b, 0.0))
            anchors = []
            while len(anchors) < n_random:
                anchors += rng.sample(originals, min(len(originals), n_random - len(anchors)))
            for a in anchors:
                other = rng.choice(others)
                pairs.append((a, rng.choice(files_of(other, "original")), 0.0))
        self.pairs = pairs


def make_augmentation(thickness=False):
    affine = v2.RandomAffine(degrees=5, translate=(0.05, 0.05), scale=(0.85, 1.0), fill=0)

    def augment(img):
        img = affine(img)
        if thickness and random.random() < 0.5:
            img = F.max_pool2d(img.unsqueeze(0), 3, stride=1, padding=1).squeeze(0)
        return img

    return augment