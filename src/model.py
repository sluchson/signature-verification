import torch.nn as nn
import torch.nn.functional as F


def conv_block(in_channels, out_channels, kernel_size):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel_size, padding=kernel_size // 2),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2),
    )


class SignatureNet(nn.Module):
    def __init__(self, embedding_dim=128, dropout=0.3):
        super().__init__()
        self.features = nn.Sequential(
            conv_block(1, 32, 5),
            conv_block(32, 64, 3),
            conv_block(64, 128, 3),
            conv_block(128, 128, 3),
        )
        self.pool = nn.AdaptiveAvgPool2d((2, 4))
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(128 * 2 * 4, embedding_dim)

    def embed(self, x):
        x = self.features(x)
        x = self.pool(x).flatten(1)
        x = self.fc(self.dropout(x))
        return F.normalize(x, dim=1)

    def forward(self, a, b):
        return F.pairwise_distance(self.embed(a), self.embed(b))


def contrastive_loss(distance, label, margin=1.0):
    positive = label * distance.pow(2)
    negative = (1 - label) * F.relu(margin - distance).pow(2)
    return (positive + negative).mean()