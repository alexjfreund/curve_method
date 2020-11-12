# The Curvature Method

A quantitative approach to select the optimal number of clusters in a dataset.

## Table of contents
* [Introduction](#introduction)
* [Installation](#installation)
* [Examples](#examples)
* [Dependencies](#dependencies)
* [References](#references)

## Introduction

Clustering is a major area in Unsupervised Machine Learning. In many
clustering algorithms, the number of desired clusters is given as a
parameter. Selecting a dataset's true cluster number _k_ can be 
challenging, as model accuracy increases with additional clusters, yet 
too high of a _k_ value leads to overfitting, and a less meaningful model. 
Because the value of _k_ has a dramatic impact on clustering results, 
it is important to select it carefully.

The most common method of selecting a true cluster number is known as
the "Elbow Method", which involves manually selecting a point along an
evaluation graph that appears to contain the sharpest corner. There are
several problems with this approach, as it is empirical and requires direct
intervention. Additionally, the axes of the evaluation graph tend to lie on 
significantly different scales, which makes it difficult to recognize the 
optimal _k_ value visually. In contrast, the Curvature Method is a recent 
approach that quantitatively finds the optimal _k_ value [[1]](#1). This 
approach can be used in a broad range of clustering applications, further 
decoupling the learning process from human intervention.

## Installation
* TODO

## Examples
To view the curvature index for each _k_ value, use the curve_scores() 
function:
```
from curve_method import curve_scores

X, _ = make_blobs(n_samples=10000, n_features=4, centers=5)
curve_scores(X, k_max=10)
```

Or, to just obtain the _k_ value with maximum curvature, use the true_k()
function:
```
from curve_method import true_k

X, _ = make_blobs(n_samples=10000, n_features=4, centers=5)
true_k(X, k_max=10)
```

To help interpret results, the curve_method package can also produce an 
evaluation graph for a range of _k_ values. To do this, use the scatter() 
function:
```
from curve_method import scatter

X, _ = make_blobs(n_samples=10000, n_features=4, centers=5)
scatter(X, k_max=12, line=False)
```

Finally, the curve_method can also show an approximation of the evaluation 
graph. This can be done with the polyfit() function:
```
from curve_method import polyfit

X, _ = make_blobs(n_samples=10000, n_features=4, centers=5)
polyfit(X, k_max=12, deg=3)
```

## Dependencies
* NumPy
* Matplotlib
* Scikit-learn

## References
<a name="1"></a>
Zhang, Y., Mańdziuk, J., Quek, C.H. and Goh, B.W., 2017.
Curvature-based method for determining the number of clusters.
Information Sciences, 415, pp.414-428.

## License
This project is licensed under the terms of the MIT License (see the file LICENSE).