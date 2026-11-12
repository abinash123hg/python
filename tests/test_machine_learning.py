import unittest

import numpy as np

from machine_learning.kmeans import KMeans
from machine_learning.linear_regression import LinearRegression
from machine_learning.logistic_regression import LogisticRegression


class LinearRegressionTest(unittest.TestCase):
    def test_recovers_weights_and_bias(self):
        rng = np.random.default_rng(42)
        X = rng.normal(size=(200, 3))
        y = X @ np.array([2.0, -1.5, 0.5]) + 3.0
        model = LinearRegression().fit(X, y)
        self.assertGreater(model.score(X, y), 0.95)
        np.testing.assert_allclose(model.weights, [2.0, -1.5, 0.5], atol=0.1)


class LogisticRegressionTest(unittest.TestCase):
    def test_separates_two_blobs(self):
        rng = np.random.default_rng(7)
        X = np.vstack([rng.normal(-2, 1, (100, 2)), rng.normal(2, 1, (100, 2))])
        y = np.array([0] * 100 + [1] * 100)
        model = LogisticRegression().fit(X, y)
        self.assertGreater(model.accuracy(X, y), 0.95)


class KMeansTest(unittest.TestCase):
    def test_finds_three_clusters(self):
        rng = np.random.default_rng(0)
        X = np.vstack([rng.normal(c, 0.5, (50, 2)) for c in ((0, 0), (6, 6), (0, 6))])
        model = KMeans(k=3).fit(X)
        for center in ((0, 0), (6, 6), (0, 6)):
            distances = ((model.centroids - np.array(center)) ** 2).sum(axis=1)
            self.assertLess(distances.min(), 1.0)


if __name__ == "__main__":
    unittest.main()
