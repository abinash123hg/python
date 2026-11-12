"""Linear regression trained with full-batch gradient descent (numpy)."""

import numpy as np


class LinearRegression:
    """Fits y = X @ w + b by minimising mean squared error."""

    def __init__(self, learning_rate=0.05, epochs=500):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0.0

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        n_samples = X.shape[0]
        self.weights = np.zeros(X.shape[1])
        self.bias = 0.0
        for _ in range(self.epochs):
            error = X @ self.weights + self.bias - y
            self.weights -= self.learning_rate * (X.T @ error / n_samples)
            self.bias -= self.learning_rate * error.mean()
        return self

    def predict(self, X):
        return np.asarray(X, dtype=float) @ self.weights + self.bias

    def score(self, X, y):
        """Coefficient of determination (R^2)."""
        y = np.asarray(y, dtype=float)
        residual = y - self.predict(X)
        return 1 - np.sum(residual**2) / np.sum((y - y.mean()) ** 2)


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    X = rng.normal(size=(200, 3))
    true_weights = np.array([2.0, -1.5, 0.5])
    y = X @ true_weights + 3.0 + rng.normal(scale=0.1, size=200)
    model = LinearRegression().fit(X, y)
    print("learned weights:", np.round(model.weights, 3), "bias:", round(model.bias, 3))
    print("R^2:", round(model.score(X, y), 4))
