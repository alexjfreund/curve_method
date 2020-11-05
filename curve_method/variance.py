import math
from sklearn.cluster import KMeans

# compute the total within-cluster variance for all clusters
def cluster_variance(X, centroids, labels):
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

# compute a list of variance scores for each k-value
def variance_list(X, k_values):
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

# compute change in variance for each k with respect to the previous k-value
def variance_deltas(X, k_max):
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
    # return a list of variance deltas
    return deltas

# compute a dictionary containing curvature indices for each k-value
def curvature_indices(X, k_max):
    deltas = variance_deltas(X, k_max)
    indices = {}
    # compute curvature index for all k-values from k=2 to k=k_max
    for k in range(2, k_max + 1):
        indices[k] = deltas[k] / deltas[k + 1]
    return indices
