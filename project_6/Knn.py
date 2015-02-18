# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 04:24:43 2014

@author: RahulKapur
"""


#Rahul Kapur
#rk2749
import numpy as np
import scipy as sp
from copy import deepcopy


def make_data (file_name):
    inputFile = open(file_name, 'r') # open file
    changeFunction = lambda x: 1 if (x == "M") else 0 #replace malignant and begnign with 1 or 0
    array = np.loadtxt(inputFile, delimiter= ',', dtype= float, converters={1: changeFunction}) #load data from file
    array = sp.delete(array, 0 , 1) #delete the first column of array
    #print array
    return array

def split_data(data, p):
    rows = len(data) #number of rows
    columns = len(data[0]) #number of columns
    division = float((p -1))/p #division fraction
    unroundedRowDivider = rows * division
    if (unroundedRowDivider % 1 != 0):
        rowDivider = int(rows * division) + 1 # row division
    else:
        rowDivider = int(rows * division)
    
    trainingArray  = np.zeros((rowDivider, columns)) #training array
    testArray = np.zeros(((rows - rowDivider), columns)) #test array
    for i in range (0, rows):
        for j in range (0, columns):
            if (i < rowDivider ):
                trainingArray[i][j] = data[i][j] #populate training array
            else:
                testArray[i - rowDivider][j] = data[i][j]


    tuple = (trainingArray, testArray)

    return tuple # return the tuple
    
def NNclassifier( training, test): #
    trainingArray = np.delete(training, 0, 1)
    rowTest  = len(test) #row length of test
    rowTraining = len(training) # row length of training
    jValues = np.zeros((rowTest)) #jValue array
    for i in range(0 , rowTest): #loop through test
        number = 0 #euclidean dist
        counter = 0 #counter
        value = 0#0 or 1
        for j in range (0, rowTraining):
            counter = counter + 1
            differenceArray = trainingArray[j] - test[i]
            squaredArray = differenceArray ** 2
            sum = np.sum(squaredArray)
            sum = sum ** (0.5)
            if(counter == 1): #first element
                number = sum
                value = training[j][0]
            if (number > sum):#find smallest value
                number = sum
                value = training[j][0]#set value
        jValues[i] = value #append value to array
        

    return jValues
    
def KNNclassifier(training, test, k):
    trainingArray = np.delete(training, 0, 1)
    rowTest  = len(test) #row length of test
    rowTraining = len(training) # row length of training
    jValues = np.zeros((rowTest)) #jValue array
    kList = []
    oneOrZeroValue = []
    for i in range(0 , rowTest): #loop through test
        number = 0 #euclidean dist
        counter = 0 #counter
        for j in range (0, rowTraining): #number of rows
            counter = counter + 1 #increment counter
            differenceArray = trainingArray[j] - test[i] #dind difference
            squaredArray = differenceArray ** 2 #square the items
            sum = np.sum(squaredArray) #sum the values
            sum = sum ** (0.5) #square root the sum
            if (len(kList) != k): #if it is the first k value
                kList.append(sum) #append to this list
                oneOrZeroValue.append(training[j][0]) 
            else:
                positionCounter = 0 #positions counter
                maxNumber = -1 #maxValue in kList
                maxPosition = -1 #position in list for max k value
                for number in kList: #loop through the list
                    if (maxNumber == -1): #set max number and position
                        maxNumber = number
                        maxPosition = positionCounter
                    if (maxNumber > number): #find maxValue
                        maxNumber = number
                        maxPosition = positionCounter
                    positionCounter = positionCounter + 1
                if (int(maxNumber) > sum): #if maxValue is greater than sum
                    kList[maxPosition] = sum #replace maxValue with sum
                    oneOrZeroValue[maxPosition] = training[j][0] 
        oneCounter = 0 #number of 1 in the list
        for item in oneOrZeroValue:
            if (int(item) == 1):#if 1
                oneCounter = oneCounter + 1 # increment
        if (k-oneCounter < oneCounter):
            jValues[i] = 1 #set jValue
        else:
            jValues[i] = 0 #set jValue
    return jValues
    
def n_validator(data, p, classifier,*args):
    mValue = len(data) #m value
    sum = 0 # score counter
    np.random.shuffle(data) #randomize rows
    splitArray = np.array_split(data, p) # split data into p sections
    for i in range(0, len(splitArray)): #loop through each subArray
        testArray = splitArray[i] # store testArray
        trainingArray = np.zeros((1)) #create training array
        counter = 0 
        for j in range (0, len(splitArray)): #loop through splitarray
            if (j != i): #put the other data in training array
                if(counter == 0):
                    counter = 1
                    trainingArray = splitArray[j]
                else:
                    trainingArray = np.append(trainingArray, splitArray[j], 0)
        testArrayCopy = deepcopy(testArray) # create copy of test
        numberOfRowsTest = len(testArray) #rows in test
        actualResultsArray = np.zeros((numberOfRowsTest)) #correct 0 or 1 value        
        kValue = args[0] #store kValue     
        for i in range (0, numberOfRowsTest):#loop through test array
            actualResultsArray[i] = testArray[i][0] #store actual results
        testArrayCopy = sp.delete(testArrayCopy, 0 , 1) #delete copy results
        testResultsArray = classifier(trainingArray,testArrayCopy, kValue)
        for i in range (0,len(testResultsArray)): #loop through test results
            if (testResultsArray[i] == actualResultsArray[i]):
                sum = sum + 1 #increment counter for corresponding results
    
    finalValue = sum/float(mValue) #divide by mValue
    
    return finalValue # return final value      
    
    
    
    
    





