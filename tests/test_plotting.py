import unittest
from sklearn.datasets import make_blobs
from curve_method import scatter, polyfit
class TestPlotting(unittest.TestCase):

    # validate execution of scatter function without a line
    def test_scatter(self):
        blobs, _ = make_blobs(n_samples=100, n_features=2, centers=4)
        scatter(blobs, k_max=12, line=False)

    # validate execution of scatter function with line drawn
    def test_scatter_line(self):
        blobs, _ = make_blobs(n_samples=100, n_features=2, centers=4)
        scatter(blobs, k_max=12, line=True)

    # validate execution of polyplot function with degree=3
    def test_polyplot_3(self):
        blobs, _ = make_blobs(n_samples=100, n_features=2, centers=4)
        polyfit(blobs, k_max=12, deg=3)

    # validate execution of polyplot function with degree=5
    def test_polyplot_5(self):
        blobs, _ = make_blobs(n_samples=100, n_features=2, centers=4)
        polyfit(blobs, k_max=12, deg=5)

if __name__ == '__main__':
    unittest.main()
