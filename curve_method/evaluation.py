import numpy as np
from .validation import validate_k, validate_deg
from .variance import curvature_indices

def curve_scores(X, k_max=12):
    """
    Returns the curvature index for each k-value in the range [2, k_max].

    Parameters
    ----------
    X : ndarray
        A 2D array of input data where each row represents a sample and 
        each column represents a feature.
    k_max : int
        The maximum desired k-value.
    
    Returns
    -------
    dict
        The computed curvature index of each k-value, where k is the key 
        and index is the value.
    """
    validate_k(k_max)
    indices = curvature_indices(X, k_max)
    # return list of curvature indices
    return indices

def true_k(X, k_max=12):
    """
    Returns the k-value with maximum curvature index value in the range [2, k_max].

    Parameters
    ----------
    X : ndarray
        A 2D array of input data where each row represents a sample and 
        each column represents a feature.
    k_max : int
        The maximum desired k-value.
    
    Returns
    -------
    int
        The k-value with the highest curvature index value.
    """
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
