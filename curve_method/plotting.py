import numpy as np
import matplotlib.pyplot as plt
from .validation import validate_k, validate_deg
from .variance import variance_list
    
def scatter(X, k_max=12, line=False):
    validate_k(k_max)
    k_values = range(1, k_max + 1)
    v_values = variance_list(X, k_values)
    plt.scatter(k_values, v_values)
    if line:
        plt.plot(k_values, v_values)
    plt.title("Evaluation Graph")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Within-Cluster Variance")
    plt.show()

def polyfit(X, k_max=12, deg=3):
    validate_k(k_max)
    validate_deg(deg)
    k_values = range(1, k_max + 1)
    v_values = variance_list(X, k_values)
    coefs = np.polyfit(k_values, v_values, deg)
    formula = np.polyval(coefs, k_values)
    plt.plot(k_values, formula)
    plt.scatter(k_values, v_values)
    plt.title("Approximation of Evaluation Graph")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Within-Cluster Variance")
    plt.show()
