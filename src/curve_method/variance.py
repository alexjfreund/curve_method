import math
from sklearn.cluster import KMeans

def cluster_variance(X, centroids, labels):
    total = 0
    for i in range(X.shape[0]):
        instance = X[i]
        cluster_id = labels[i]
        center = centroids[cluster_id]
        for j in range(X.shape[1]):
            total += math.pow(instance[j] - center[j], 2)
    return total

def variance_list(X, k_values):
    within_vars = []
    for k in k_values:
        kmeans = KMeans(n_clusters=k).fit(X)
        y = kmeans.predict(X)
        total_v = cluster_variance(X, kmeans.cluster_centers_, y)
        within_vars.append(total_v)
    return within_vars
    
def variance_deltas(X, k_max):
    scores = {}
    deltas = {}
    for k in range(1, k_max + 2):
        v_values = []
        for t in range(3):
            kmeans = KMeans(n_clusters=k).fit(X)
            y = kmeans.predict(X)
            total_v = cluster_variance(X, kmeans.cluster_centers_, y)
            v_values.append(total_v)
        scores[k] = min(v_values)
        if k > 1:
            deltas[k] = scores[k] - scores[k - 1]
    return deltas

def curvature_indices(X, k_max):
    deltas = variance_deltas(X, k_max)
    indices = {}
    for k in range(2, k_max + 1):
        indices[k] = deltas[k] / deltas[k + 1]
    return indices
