import numpy as np
import matplotlib.pyplot as plt
from .validation import validate_k, validate_deg
from .variance import variance_list

def scatter(X, k_max=12, line=False):
    '''
    Generates an evaluation scatter plot of within-cluster variance 
    at each k-value in the range [2, k_max].

    Parameters
    ----------
    X : 2darray
        An array of input data where each column represents a feature and 
        each row represents a sample.
    k_max : int
        The maximum desired k-value.
    line : bool
        Specify whether to connect points with a line.
    '''
    validate_k(k_max)
    # set x axis scale for graph
    k_values = range(1, k_max + 1)
    # set y axis values for graph
    v_values = variance_list(X, k_values)
    plt.scatter(k_values, v_values)
    # if desired, connect scatter points with a line
    if line:
        plt.plot(k_values, v_values)
    plt.title("Evaluation Graph")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Within-Cluster Variance")
    plt.show()

def polyfit(X, k_max=12, deg=3):
    '''
    Generates a polynomial approximation graph of within-cluster variance
    at each k-value in the range [2, k_max] according to a certain polynomial
    degree.

    Parameters
    ----------
    X : 2darray
        An array of input data where each column represents a feature and 
        each row represents a sample.
    k_max : int
        The maximum desired k-value.
    deg : int
        The desired polynomial degree.
    '''
    validate_k(k_max)
    validate_deg(deg)
    # set x axis scale for graph
    k_values = range(1, k_max + 1)
    # set y axis values for graph
    v_values = variance_list(X, k_values)
    # compute polynomial coefficients for best fitting line
    coefs = np.polyfit(k_values, v_values, deg)
    # use coefficients to generate an approximation function
    formula = np.polyval(coefs, k_values)
    plt.plot(k_values, formula)
    plt.scatter(k_values, v_values)
    plt.title("Approximation of Evaluation Graph")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Within-Cluster Variance")
    plt.show()
