import numpy as np
from .validation import validate_k, validate_deg
from .variance import curvature_indices

def curve_scores(X, k_max=12):
    validate_k(k_max)
    indices = curvature_indices(X, k_max)
    return indices

def true_k(X, k_max=12):
    indices = curve_scores(X, k_max)
    max_index = -np.Inf
    best_k = -1
    for k in range(2, k_max + 1):
        if indices[k] > max_index:
            max_index = indices[k]
            best_k = k
    return best_k
