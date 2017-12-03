# Created on Tue Mar 2 2016
# @author: vipulkhatana 

import csv
import numpy as np 
import matplotlib.pyplot as plt 
import math 
import itertools 
import pandas as pd 

#  Initial centroids 
def icentroid(X_Matrix, centroid, k, n,p):
    for i in range(k):
        for j in range(2):
            centroid[i,j] = X_Matrix[((k+p*(i))%n),j]

# Initial clusters
def icluster(X, mnew):
    for i in range (n):
        min = 100000000
        for j in range (k): 
            distance = np.linalg.norm(X[i]- c[j])
            if (distance < min):
                min = distance 
                index = j
            else :
                mnew[i,j] = 0 
        mnew[i,index] = 1

# execution of the E-M step
def main(X, mold, mnew) : 
    for iteration in range (500) : 
        check = True
        for i in range (n):
            for j in range (k):
                if (mnew[i,j] != mold[i,j]):
                    check = False
        if (check):
            break 
        else : 
            mold = mnew 
            
            def ncentroid(X) :
                for i in range (k) :
                    sum = 0
                    num = 0
                    for j in range(n):
                        if (mnew[j,i] == 1) :
                            num = num + 1
                            sum = sum + mnew[i,j]
                    c[i] = sum/num 

            def ncluster(X) : 
                min = 100000000
                for i in range(n) : 
                    for j in range(k): 
                        distance = np.linalg.norm(X[i]-c[j])
                        if (distance<min) :
                            min = distance 
                            index = j 
                        else :
                            mnew[i,j] = 0 
                    mnew[i,index] = 1

# cost function
def cost(X): 
    cost = 0
    for i in range (k):
        for j in range (n):
            if (mnew[j,i] == 1):
                dist = np.linalg.norm(X[j]-c[i])
                cost = cost + dist*dist 

# assign labels
def label(X, mnew, lab):
    #lab = np.zeros((1,n),dtype=float)
    for j in range (k): 
        for i in range(n): 
            if (mnew[i,j] == 1):
                lab[0,i] = j
       
X_1 = np.loadtxt(sys.argv[1],dtype=float)
X_2 = np.loadtxt(sys.argv[1],dtype=float)
X_3 = np.loadtxt(sys.argv[1],dtype=float)

n= 790
k=10
min = 100000000
iteration =0 
size = n%k 
mold_1 = np.zeros((n,k),dtype=float)
mnew_1 = np.zeros((n,k),dtype=float)
c = np.zeros((k,2),dtype=float)
min = 100000000
index=0 
lab_1 = np.zeros((1,n),dtype=float)
    
icentroid(X_1, c, k ,n,14) 
icluster(X_1, mnew_1)
main(X_1, mold_1, mnew_1)
label(X_1, mnew_1, lab_1)

np.savetxt("label.csv",lab_1)
np.savetxt("final_centroid_<2014EE10495>.txt", c)

#*******TESTING******###

n= 790
k=10
min = 100000000
X_1 = np.loadtxt('train_data.csv',dtype=float)
X_2 = np.loadtxt('train_data.csv',dtype=float)
X_3 = np.loadtxt('train_data.csv',dtype=float)
c = np.zeros((k,2),dtype=float)
mnew_1 = np.zeros((n,k),dtype=float)
lab_1 = np.zeros((1,n),dtype=float)
centroid = np.loadtxt('final_centroid_<2014EE10495>.txt', dtype = float)

def ncluster(X,c) : 
    min = 100000000
    for i in range(n) : 
        for j in range(k): 
            distance = np.linalg.norm(X[i]-c[j])
            if (distance<min) :
                min = distance 
                index = j 
            else :
                mnew_1[i,j] = 0 
            mnew_1[i,index] = 1

ncluster(X_1,centroid)
label(X_1,mnew_1,lab_1)

np.savetxt("test_predicted_class_label_<2014EE10495>.csv",lab_1)
