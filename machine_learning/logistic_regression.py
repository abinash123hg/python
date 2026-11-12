"""Binary logistic regression trained with gradient descent (numpy)."""

import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


class LogisticRegression:
    """Fits P(y=1|x) = sigmoid(x @ w + b) by minimising binary cross-entropy."""

    def __init__(self, learning_rate=0.1, epochs=1000):
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
            error = sigmoid(X @ self.weights + self.bias) - y
            self.weights -= self.learning_rate * (X.T @ error / n_samples)
            self.bias -= self.learning_rate * error.mean()
        return self

    def predict_proba(self, X):
        return sigmoid(np.asarray(X, dtype=float) @ self.weights + self.bias)

    def predict(self, X):
        return (self.predict_proba(X) >= 0.5).astype(int)

    def accuracy(self, X, y):
        return float(np.mean(self.predict(X) == np.asarray(y, dtype=int)))


if __name__ == "__main__":
    rng = np.random.default_rng(7)
    X = np.vstack([rng.normal(-2, 1, (100, 2)), rng.normal(2, 1, (100, 2))])
    y = np.array([0] * 100 + [1] * 100)
    model = LogisticRegression().fit(X, y)
    print("train accuracy:", round(model.accuracy(X, y), 4))
