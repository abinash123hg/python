"""K-means clustering (Lloyd's algorithm) implemented with numpy."""

import numpy as np


class KMeans:
    """Groups samples into k clusters by iteratively assigning points to the
    nearest centroid and recomputing centroids.

    Centroids are seeded with k-means++ and the whole procedure is repeated
    ``restarts`` times, keeping the run with the lowest inertia (the same
    strategy sklearn uses with ``n_init``).
    """

    def __init__(self, k, max_iterations=100, seed=0, restarts=5):
        self.k = k
        self.max_iterations = max_iterations
        self.seed = seed
        self.restarts = restarts
        self.centroids = None
        self.labels = None

    def _seed_centroids(self, X, rng):
        """k-means++ seeding: each new centroid is sampled proportional to its
        squared distance from the nearest existing centroid."""
        centroids = [X[rng.integers(X.shape[0])]]
        for _ in range(1, self.k):
            squared = ((X[:, None, :] - np.array(centroids)[None, :, :]) ** 2).sum(-1)
            probs = squared.min(axis=1)
            probs = probs / probs.sum()
            centroids.append(X[rng.choice(X.shape[0], p=probs)])
        return np.array(centroids)

    def _fit_once(self, X, rng):
        centroids = self._seed_centroids(X, rng)
        labels = None
        for _ in range(self.max_iterations):
            distances = ((X[:, None, :] - centroids[None, :, :]) ** 2).sum(-1)
            labels = distances.argmin(axis=1)
            updated = np.array(
                [X[labels == j].mean(axis=0) if (labels == j).any() else centroids[j]
                 for j in range(self.k)]
            )
            if np.allclose(updated, centroids):
                centroids = updated
                break
            centroids = updated
        return centroids, labels

    def fit(self, X):
        X = np.asarray(X, dtype=float)
        rng = np.random.default_rng(self.seed)
        best = None
        for _ in range(self.restarts):
            centroids, labels = self._fit_once(X, rng)
            inertia = float(((X - centroids[labels]) ** 2).sum())
            if best is None or inertia < best[0]:
                best = (inertia, centroids, labels)
        _, self.centroids, self.labels = best
        return self

    def inertia(self, X):
        """Sum of squared distances from each sample to its centroid."""
        X = np.asarray(X, dtype=float)
        return float(((X - self.centroids[self.labels]) ** 2).sum())


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = np.vstack([rng.normal(c, 0.6, (50, 2)) for c in ((0, 0), (5, 5), (0, 5))])
    model = KMeans(k=3).fit(X)
    order = np.argsort(model.centroids[:, 0])
    print("centroids:\n", np.round(model.centroids[order], 2))
    print("inertia:", round(model.inertia(X), 2))
