"""Train a small MLP in PyTorch on synthetic two-class data (CPU friendly)."""

import torch
from torch import nn


def make_dataset(n_per_class=250, seed=0):
    """Two gaussian clouds in 4-D, labelled 0 and 1."""
    gen = torch.Generator().manual_seed(seed)
    negative = torch.randn(n_per_class, 4, generator=gen) - 1.0
    positive = torch.randn(n_per_class, 4, generator=gen) + 1.0
    X = torch.cat([negative, positive])
    y = torch.cat([torch.zeros(n_per_class, dtype=torch.long),
                   torch.ones(n_per_class, dtype=torch.long)])
    return X, y


def train(epochs=30, learning_rate=0.01, seed=0):
    """Full-batch training loop; returns (model, train accuracy)."""
    torch.manual_seed(seed)
    X, y = make_dataset()
    model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 2))
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    for _ in range(epochs):
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        accuracy = (model(X).argmax(dim=1) == y).float().mean().item()
    return model, accuracy


if __name__ == "__main__":
    _, accuracy = train()
    print("final train accuracy:", round(accuracy, 4))
