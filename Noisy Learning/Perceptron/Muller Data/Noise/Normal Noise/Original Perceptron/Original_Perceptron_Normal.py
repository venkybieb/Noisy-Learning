import random
import os
import csv
import numpy as np
from numpy.linalg import norm
import perceptron
import math
from data import func


def perceptron_pred(x, w, noise):

    total = 0
    noise = np.random.normal(0,noise,1)
    total = np.dot(w,x)
    total += noise

    if (total < 0):
        return -1
    else:
        return 1


def train_perceptron(X, Y, w, no, a):

    i = 0
    for row in X:
        l = perceptron_pred(row,w,no)
        if (l != Y[i]):
            w = w + (Y[i]*row)
        if (a == 0):
            w_norm = norm(w,2)
            if (w_norm != 0):
                w = w/w_norm
        i+=1
    return w


def test_perceptron_no_noise(X, Y, w):
    
    i = 0
    error = 0
    total = 0
    for row in X:
        total_val = np.dot(w,row)
        if (total_val < 0):
            l = -1
        else:
            l = 1
        if (l != Y[i]):
            error += 1
        total += 1
        i+= 1
    return (total-error)/total


def test_perceptron_noise(X, Y, w, std,first,second):
     
    i = 0
    acc_error = 0
    acc_total_sum = 0
    total =  0
    val = 0

    for row in X:

        total_val = np.dot(w,row)
        noise = np.random.normal(0,std,1)
        total_val += noise[0]
        
        if (total_val < 0):
            pred = -1
        else:
            pred = 1

        if (pred != Y[i]):
            acc_error += 1

        acc_total_sum += 1
        i+= 1
        
    return (acc_total_sum-acc_error)/acc_total_sum



dim_list=  [30,100]



 
for dim in dim_list:

    train_data,train_labels,test_data,test_labels = func(0.7,dim)

    train_data = np.array(train_data)
    train_labels = np.array(train_labels)
    test_data = np.array(test_data)
    test_labels = np.array(test_labels)
    
   

    

    for std in range(1,11,1):

        acc =0

        for i in range(100):
                
            w = np.zeros((1,train_data.shape[1]))
            
            for j in range(10):

                w = train_perceptron(train_data,train_labels,w,0)

                
            accuracy= test_perceptron_noise(test_data, test_labels, w,std,first,second)

            acc+=((accuracy)*100)

        acc = acc/100
           
