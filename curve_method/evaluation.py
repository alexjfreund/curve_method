import numpy as np
from .validation import validate_k, validate_deg
from .variance import curvature_indices

# obtain curvature indices for all k-values up to a specified maximum
def curve_scores(X, k_max=12):
    validate_k(k_max)
    indices = curvature_indices(X, k_max)
    # return list of curvature indices
    return indices

# obtain the k-value with the highest curvature index
def true_k(X, k_max=12):
    indices = curve_scores(X, k_max)
    max_index = -np.Inf
    best_k = -1
    # consider all k-values from k=2 to k=k_max
    for k in range(2, k_max + 1):
        if indices[k] > max_index:
            max_index = indices[k]
            best_k = k
    # return the optimal k-value
    return best_k
