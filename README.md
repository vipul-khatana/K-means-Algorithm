# K-means-Algorithm
In this code I have tried to implement the basic k-means algorithm. 

## Overview 
K-means is one of the most important clustering algorithm. Given a data set we can find the clusters of points which have almost equal distance to a common point. This common point is called the median of a cluster. So given a dataset we find out the optimal number of clusters and a set of centroids, each centroid is associated with a cluster. Every point in the cluster has the minimum distance with it's respective centroid as compared to all other centroids. 

## Basic Principles Used 

Initially we chose a certain number of clusters. Then according to this number we initialise the number of centroids. Every point in the data set has its distance measured with these centroids. The centroid with which a point has the minimum distance gets labeled as part of the cluster of that centroid. After this iteration is completed, we calculate the overall mean square error. Then gradient descent is applied to update the values of the clusters. 

Different number of clusters are chosen and the accuracy is obtained for each of them. It is observed that the accuracy reaches a maximum for a certain number of clusters and then remains constant. 

## Installation 
