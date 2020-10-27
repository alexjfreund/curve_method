# The Curvature Method

This project contains a novel implementation of the Curvature Method for determining the optimal number of clusters in a data set. My implementation is based on a paper published in _Information Sciences_ (2017) [[1]](#1).

## Table of contents
* [Introduction](#introduction)
* [Dependencies](#dependencies)
* [Setup](#setup)
* [Examples](#examples)
* [References](#references)

## Introduction
Clustering is a major area in Unsupervised Machine Learning. In many clustering algorithms, the number of desired clusters is given as a parameter. Selecting the true cluster number (_k_) can be challenging, as model accuracy increases indefinitely with additional clusters, yet the results become less meaningful. Because the value of _k_ has a dramatic impact on results, it is important to select it carefully. The Curvature Method is a recent approach to this problem, and can be used whenever a desired _k_ value is needed.

The most common method of selecting a true cluster number is known as the "Elbow Method", which involves manually selecting a point along an evaluation graph that appears to contain the sharpest corner. This approach has several problems, as it is empirical and often fails to reveal a clear answer. In contrast, the Curvature Method is quantitative and can be performed quickly to result in an optimal _k_ value, further decoupling the learning process from human intervention.

## Dependencies
* TODO

## Setup
* TODO

## Examples
* TODO

## References
<a id="1">[1]</a>
Zhang, Y., Mańdziuk, J., Quek, C.H. and Goh, B.W., 2017.
Curvature-based method for determining the number of clusters.
Information Sciences, 415, pp.414-428.