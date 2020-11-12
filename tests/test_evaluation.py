import unittest
from sklearn.datasets import make_blobs
from curve_method import curve_scores, true_k
class TestEvaluation(unittest.TestCase):

    # validate return format of curve_scores for n=100, features=2, centers=4
    def test_small_curve(self):
        blobs, _ = make_blobs(n_samples=100, n_features=2, centers=4)
        scores = curve_scores(blobs, k_max=12)
        self.assertEqual(len(scores), 11)
        for k in range(2, 13):
            self.assertTrue(k in scores)
            self.assertTrue(isinstance(scores[k], float))

    # validate return format of curve_scores for n=200, features=8, centers=12
    def test_big_curve(self):
        blobs, _ = make_blobs(n_samples=200, n_features=8, centers=12)
        scores = curve_scores(blobs, k_max=18)
        self.assertEqual(len(scores), 17)
        for k in range(2, 19):
            self.assertTrue(k in scores)
            self.assertTrue(isinstance(scores[k], float))

    # validate return format of true_k for n=100, features=2, centers=4
    def test_small_k(self):
        blobs, _ = make_blobs(n_samples=100, n_features=2, centers=4)
        k = true_k(blobs, k_max=12)
        self.assertTrue(isinstance(k, int))
        self.assertTrue(k >= 2)
        self.assertTrue(k <= 12)

    # validate return format of true_k for n=200, features=8, centers=12
    def test_big_k(self):
        blobs, _ = make_blobs(n_samples=200, n_features=8, centers=12)
        k = true_k(blobs, k_max=18)
        self.assertTrue(isinstance(k, int))
        self.assertTrue(k >= 2)
        self.assertTrue(k <= 18)

if __name__ == '__main__':
    unittest.main()
