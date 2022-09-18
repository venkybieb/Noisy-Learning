import random
import os
import csv
import numpy as np
from numpy.linalg import norm
import perceptron
import math
from data import func


def perceptron_pred(x, w):

    total = np.dot(w,x)

    if (total < 0):
        return -1
    else:
        return 1


def train_perceptron(X, Y, w, is_norm):

    i = 0
    
    for row in X:
        
        pred = perceptron_pred(row,w)
        
        if (pred != Y[i]):
            w = w + (Y[i]*row)
            
        if (is_norm == 0):
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
                
        pred = perceptron_pred(row,w)

            
        if (pred != Y[i]):
            error += 1
        total += 1
        
        i+= 1
        
    return (total-error)/total


def test_perceptron_noise(X, Y, w, no,prob,first,second):
    i = 0
    acc_error = 0
    acc_total_sum = 0
    total = 0
  

    probs = np.random.binomial(1,p=prob,size=(w.shape[1]))
    probs = np.expand_dims(probs,1)
    probs = np.transpose(probs)
    probs[probs==0]=-4
    w = np.multiply(w,probs)

    count=0
    
    for row in X:
        
        count+=1
        
        if count==1:
            w = np.squeeze(w,axis=0)
            
        total_val = np.dot(row,w)
        
        if (total_val < 0):
            l = -1
        else:
            l = 1
     
    
        if (l != Y[i]):
            acc_error += 1
        acc_total_sum += 1
        
        i+= 1
        
    return (acc_total_sum-acc_error)/acc_total_sum


def test_perceptron_noise(X, Y, w, bound,first,second):
     
    i = 0
    acc_error = 0
    acc_total_sum = 0
    total =  0
    
    probs = np.random.binomial(1,p=prob,size=(w.shape[1]))
    probs = np.expand_dims(probs,1)
    probs = np.transpose(probs)
    probs[probs==0]=-4
    w = np.multiply(w,probs)
   
 
    for row in X:
        
        total_val=0
        
        for j in range(first):
            
            for k in range(second):

                total_val += (w[0][second*j+k]*row[(second*j)+k])

              
                
            if (total_val >= 0):
                accum+= 1

            if (total_val < 0):
                accum-=1
                    
            total_val = 0

        if (accum > int((first**0.5)+1)):
            pred = 1

        elif (accum < -int((first**(0.5)+1))):
            pred = -1

        else:
            result = np.random.binomial(1,0.5)

            if result == 1:
                pred = 1

            else:
                pred = -1
                    
        accum = 0

        if (pred != Y[i]):
            acc_error += 1

        acc_total_sum += 1
        i+= 1
        
    return (acc_total_sum-acc_error)/acc_total_sum

dim_list=  [30,100]
thirty = [(3,10),(5,6),(6,5),(10,3)]
hundred = [(2,50),(10,10),(20,5),(4,25)]
problist = []

 
for dim in dim_list:

    train_data,train_labels,test_data,test_labels = func(0.7,dim)

    train_data = np.array(train_data)
    train_labels = np.array(train_labels)
    test_data = np.array(test_data)
    test_labels = np.array(test_labels)
    
    if dim == 30:
        pairlist = thirty
    if dim == 100:
        pairlist = hundred
     

        
    for prob in problist:

        acc=0

        for i in range(100):
                
            w = np.zeros((1,train_data.shape[1]))
                
            for j in range(10):


                w = train_perceptron(train_data,train_labels,w,0)

                
            accuracy= test_perceptron_noise(XTest, yTest, w,prob,first,second)

            acc+=((accuracy)*100)

        acc = acc/100
           