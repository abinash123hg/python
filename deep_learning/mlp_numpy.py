"""Multi-layer perceptron with manual backpropagation, written from scratch in numpy."""

import numpy as np


def relu(z):
    return np.maximum(0, z)


def softmax(z):
    shifted = z - z.max(axis=1, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=1, keepdims=True)


class MLP:
    """Fully connected network: input -> hidden (ReLU) -> logits (softmax).

    Gradients are derived for cross-entropy loss with softmax output, so the
    output-layer gradient simplifies to (probs - one_hot) / batch_size.
    """

    def __init__(self, input_dim, hidden_dim, output_dim, learning_rate=0.05, seed=0):
        rng = np.random.default_rng(seed)
        self.w1 = rng.normal(scale=0.5, size=(input_dim, hidden_dim))
        self.b1 = np.zeros(hidden_dim)
        self.w2 = rng.normal(scale=0.5, size=(hidden_dim, output_dim))
        self.b2 = np.zeros(output_dim)
        self.learning_rate = learning_rate
        self._hidden = None
        self._probs = None

    def forward(self, X):
        X = np.asarray(X, dtype=float)
        self._hidden = relu(X @ self.w1 + self.b1)
        self._probs = softmax(self._hidden @ self.w2 + self.b2)
        return self._probs

    def _backward(self, X, y_onehot):
        batch = X.shape[0]
        d_logits = (self._probs - y_onehot) / batch
        self.w2 -= self.learning_rate * (self._hidden.T @ d_logits)
        self.b2 -= self.learning_rate * d_logits.sum(axis=0)
        d_hidden = (d_logits @ self.w2.T) * (self._hidden > 0)
        self.w1 -= self.learning_rate * (X.T @ d_hidden)
        self.b1 -= self.learning_rate * d_hidden.sum(axis=0)

    def fit(self, X, y, epochs=200):
        X = np.asarray(X, dtype=float)
        y_onehot = np.eye(self.w2.shape[1])[np.asarray(y, dtype=int)]
        for _ in range(epochs):
            self.forward(X)
            self._backward(X, y_onehot)
        return self

    def predict(self, X):
        return self.forward(X).argmax(axis=1)

    def accuracy(self, X, y):
        return float(np.mean(self.predict(X) == np.asarray(y, dtype=int)))


if __name__ == "__main__":
    rng = np.random.default_rng(3)
    X = np.vstack([rng.normal(-1.5, 1, (150, 4)), rng.normal(1.5, 1, (150, 4))])
    y = np.array([0] * 150 + [1] * 150)
    model = MLP(input_dim=4, hidden_dim=16, output_dim=2).fit(X, y)
    print("train accuracy:", round(model.accuracy(X, y), 4))
