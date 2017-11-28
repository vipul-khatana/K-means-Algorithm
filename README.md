# K-means-Algorithm
This code tries to implement the basic k-means algorithm. 

## Overview 
K-means is one of the most important clustering algorithm in unsupervised learning. Given a data set we can find the clusters of points which have almost equal distance to a common point. This common point is called the centroid of a cluster. So given a dataset we find out the optimal number of clusters and a set of centroids, each centroid is associated with a cluster. Every point in the cluster has the minimum distance with it's respective centroid as compared to all other centroids. 

## Basic Principles Used 

To implement k-means we use the Expectation Maximisation Algorithm also called the EM algorithm . It consists of two simple steps 
1) Initially guess the number of clusters 
2) Repeat until converged 
  + E-step: assign points to the nearest cluster 
  + M-step: set the cluster centres to the mean

Here the "E-step" or "Expectation step" is so-named because it involves updating our expectation of which cluster each point belongs to. The "M-step" or "Maximization step" is so-named because it involves maximizing some fitness function that defines the location of the cluster centers—in this case, that maximization is accomplished by taking a simple mean of the data in each cluster.

## Installation 
Following libraries are required along with python : 
numpy, matplotlib, mpl_toolkits.mplot3d, pandas. 

These libraries can be installed by using the pip installer 

If you have pip installed on your system then use `pip install library_name` to install the required library. 
If you do not have pip then please look [here](https://pip.pypa.io/en/stable/installing/) on how to install pip

## How to Run 

Keep your dataset in the same directory in a .csv format. The name of the training file should be `train_data.csv` 

In the command line run `python k-means.py`. This should output two files : 

+ - 'final_centroid.txt' containing the final centroids of the data set
+ - "test_predicted_class_label.csv" containing the class label for every point in the data set. 

## Author 

* [Vipul Khatana](https://github.com/vipul-khatana)

Course project under [**Prof. Jayadeva**](http://jayadeva.net) 

## Contributing

1) Fork it (https://github.com/vipul-khatana/Regression-models/fork)
2) Create your feature branch `git checkout -b feature/fooBar`
3) Commit your changes `git commit -am 'Add some fooBar'`
4) Push to the branch `git push origin feature/fooBar`
5) Create a new pull request 
