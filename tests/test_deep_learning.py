import unittest

import numpy as np

from deep_learning.mlp_numpy import MLP, softmax
from deep_learning.mlp_torch import train


def blobs(seed=3):
    rng = np.random.default_rng(seed)
    X = np.vstack([rng.normal(-1.5, 1, (150, 4)), rng.normal(1.5, 1, (150, 4))])
    y = np.array([0] * 150 + [1] * 150)
    return X, y


class SoftmaxTest(unittest.TestCase):
    def test_rows_sum_to_one(self):
        probs = softmax(np.array([[1.0, 2.0, 3.0], [10.0, 10.0, 10.0]]))
        np.testing.assert_allclose(probs.sum(axis=1), 1.0)


class NumpyMLPTest(unittest.TestCase):
    def test_learns_blobs(self):
        X, y = blobs()
        model = MLP(input_dim=4, hidden_dim=16, output_dim=2).fit(X, y)
        self.assertGreater(model.accuracy(X, y), 0.9)


class TorchMLPTest(unittest.TestCase):
    def test_learns_blobs(self):
        _, accuracy = train(epochs=30)
        self.assertGreater(accuracy, 0.9)


if __name__ == "__main__":
    unittest.main()
