# The Curvature Method

A quantitative approach to select the optimal number of clusters.

## Table of contents
* [Introduction] (#introduction)
* [Installation] (#installation)
* [Dependencies] (#dependencies)
* [Examples] (#examples)
* [References] (#references)

## Introduction

Clustering is a major area in Unsupervised Machine Learning. In many
clustering algorithms, the number of desired clusters is given as a
parameter. Selecting a dataset's true cluster number *k* can be 
challenging, as model accuracy increases with additional clusters, yet 
too high of a *k* value leads to overfitting, and a less meaningful model. 
Because the value of *k* has a dramatic impact on clustering results, 
it is important to select it carefully.

The most common method of selecting a true cluster number is known as
the "Elbow Method", which involves manually selecting a point along an
evaluation graph that appears to contain the sharpest corner. There are
several problems with this approach, as it is empirical and requires direct
intervention. Additionally, the axes of the evaluation graph tend to lie on 
significantly different scales, which makes it difficult to recognize the 
optimal *k* value visually. In contrast, the Curvature Method is a recent 
approach that quantitatively finds the optimal *k* value `[1] <#1>`__. This 
approach can be used in a broad range of clustering applications, further 
decoupling the learning process from human intervention.

## Installation
-  TODO

## Dependencies
-  TODO

## Examples
-  TODO

## References
<a id="1">[1]</a>
Zhang, Y., Mańdziuk, J., Quek, C.H. and Goh, B.W., 2017.
Curvature-based method for determining the number of clusters.
Information Sciences, 415, pp.414-428.
