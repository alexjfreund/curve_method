import math
from sklearn.cluster import KMeans

def cluster_variance(X, centroids, labels):
    '''
    Returns the within-cluster variance for a particular clustering solution.

    Parameters
    ----------
    X : 2darray
        An array of input data where each column represents a feature and 
        each row represents a sample.
    centroids : ndarray
        The coordinates of each cluster center, where each column
        represents an axis and each row represents a centroid.
    labels : ndarray
        The index of the cluster that each sample belongs to.
    
    Returns
    -------
    float
        The sum of within-cluster variance across all clusters.
    '''
    total = 0
    # iterate through the rows of input data
    for i in range(X.shape[0]):
        instance = X[i]
        cluster_id = labels[i]
        center = centroids[cluster_id]
        # iterate through the columns of each row
        for j in range(X.shape[1]):
            # compute the euclidean distance from this instance to its centroid
            total += math.pow(instance[j] - center[j], 2)
    # return total distance
    return total

def variance_list(X, k_values):
    '''
    Returns the total within-cluster variances for a set of k-values.

    Parameters
    ----------
    X : 2darray
        An array of input data where each column represents a feature and 
        each row represents a sample.
    k_values : list
        A range of desired k-values.
    
    Returns
    -------
    list
        Within-cluster variance for each k in k_values.
    '''
    within_vars = []
    for k in k_values:
        # perform k-means clustering on input data for each k-value
        kmeans = KMeans(n_clusters=k).fit(X)
        y = kmeans.predict(X)
        # get a total variance score for each k-value
        total_v = cluster_variance(X, kmeans.cluster_centers_, y)
        within_vars.append(total_v)
    # return a list of total variance scores
    return within_vars

def variance_deltas(X, k_max):
    '''
    Returns the change in variance from k-1 to k for each k-value in 
    the range [2, k_max].

    Parameters
    ----------
    X : 2darray
        An array of input data where each column represents a feature and 
        each row represents a sample.
    k_max : int
        The maximum desired k-value.
    
    Returns
    -------
    dict
        The change in variance for each k-value, where k is the key 
        and delta is the value.
    '''
    scores = {}
    deltas = {}
    # iterate through all k_values needed to generate curvature indices
    for k in range(1, k_max + 2):
        v_values = []
        # perform experiment 3 times to reduce deviation
        for t in range(3):
            # perform k-means clustering on input data
            kmeans = KMeans(n_clusters=k).fit(X)
            y = kmeans.predict(X)
            # get a total variance score for each k-value
            total_v = cluster_variance(X, kmeans.cluster_centers_, y)
            v_values.append(total_v)
        # keep the best (minimum) variance for each k-value
        scores[k] = min(v_values)
        # compute change in variance for all k-values >= 2
        if k > 1:
            deltas[k] = scores[k] - scores[k - 1]
    # return a dictionary of variance delta for each k
    return deltas

def curvature_indices(X, k_max):
    '''
    Returns the curvature index for each k-value in the range [2,k_max].

    Parameters
    ----------
    X : 2darray
        An array of input data where each column represents a feature and 
        each row represents a sample.
    k_max : int
        The maximum desired k-value.
    
    Returns
    -------
    dict
        The computed curvature index of each k-value, where k is the key 
        and index is the value.
    '''
    deltas = variance_deltas(X, k_max)
    indices = {}
    # compute curvature index for all k-values from k=2 to k=k_max
    for k in range(2, k_max + 1):
        indices[k] = deltas[k] / deltas[k + 1]
    # return a dictionary of curvature index for each k
    return indices
