# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 19:53:54 2014

@author: RahulKapur
"""
# Rahul Kapur
# rk2749
import datetime as datetime
import string
import csv


def make_tweets(inFile):
    tweetFile = open(inFile, 'r') #open fil
    counter = 0
    listOfDictionaries = []
    for line in tweetFile.readlines():#loop through each line
        lineList = line.split('\t')# split by tab
        counter = counter + 1 #increment counter
        locationList =lineList[0].split() #location
        lat = float(locationList[0].strip('[,]')) #latitude
        lon = float(locationList[1].strip('[,]'))#longitude
        dateStrip = lineList[2].strip()
        getTime = datetime.datetime.strptime(dateStrip, '%Y-%m-%d %H:%M:%S')
        tweetString = str(lineList[3]).lower() #lower case tweet
        tweetDictionary = {'text': tweetString, 'time': getTime, 'latitude': lat, 'longitude': lon}
        listOfDictionaries.append(tweetDictionary) #append to list
        
    return listOfDictionaries

    
    
def add_sentiment(tweets, sentiment_file):
    csvFile = open(sentiment_file, 'r')
    csvArray = csv.reader(csvFile) #read csv file
    punctuations = string.punctuation
    wordDictionary = {} #create dictionary of words
    
    for row in csvArray: #loop through csv file
        word = ""
        for char in row[0]:
            if char not in punctuations: # remove punctuations
                word = word + char
        row[0] = word #add word to row
        wordDictionary[row[0]] = row[1] #add to dictionary 
    
    for item in tweets:#loop through tweets
        sum = 0
        counter = 0
        tweetLine = item['text'] #get line of text
        for words in tweetLine.split():
            word = ""
            for char in words:
                if char not in punctuations: # remove punctuatons from words
                    word = word + char
            if word in wordDictionary:#check in dictionary
                sum = float(wordDictionary[word]) + sum #add sum
                counter = counter + 1 #increment counter
        if counter == 0: #if no words in dictionary
            item['sentiment'] = None #then sentiment is none
        else:    
            item['sentiment'] = float(sum/counter) #else sum/counter
            
        outputFile = open("/Users/RahulKapur/Desktop/outputfile.txt", 'w')  
    for item in tweets:#write to output file
        outputFile.write(str(item['latitude']) + "\t")
        outputFile.write(str(item['longitude']) + "\t")
        outputFile.write(str(item['time']) + "\t")
        outputFile.write(str(item['sentiment']) + "\t")
        outputFile.write(item['text'])
        
    outputFile.close() #close file

def readNewFileWithSentiment(outputFile):#readNewSentiment
    output = open(outputFile, 'r')
    listOfDictionaries = []
    for line in output.readlines(): #loop through lines of file
        lineList = line.split('\t') #split line
        lat = float(lineList[0].strip('[,]'))
        lon = float(lineList[1].strip('[,]'))
        dateStrip = lineList[2].strip() #strip date
        getTime = datetime.datetime.strptime(dateStrip, '%Y-%m-%d %H:%M:%S')
        tweetString = str(lineList[4]).lower()
        if lineList[3] == "None":
            sentimentFloat = None #set sentiment 
        else:
            sentimentFloat = float(lineList[3])
        tweetDictionary = {'text': tweetString, 'time': getTime}
        tweetDictionary['latitude'] = lat  #add to dictionary
        tweetDictionary['longitude'] = lon  #add to dictionary
        tweetDictionary['sentiment'] = sentimentFloat
        listOfDictionaries.append(tweetDictionary) #append to list
    output.close() #close file
    return listOfDictionaries #return list

def avg_sentiment(tweets):
    counter = 0
    sum = 0 #sentiment sum
    for item in tweets:
        if item['sentiment'] != None: #if not none
            sum = item['sentiment'] + sum #add sentiment value
            counter = counter + 1 #increment counter
    if counter != 0:
        finalValue = float(sum/counter)
    else:
        finalValue = None
    return finalValue #return average value
    
def tweet_filter(tweets,*args): #tweet filet
    punctuations = string.punctuation#punctuations
    listofTweets = [] #list of new tweets
    for item in tweets: #loop through tweets
        wordCounter = 0 #words found in string
        argumentCounter = 0 #number of arguments passed
        for argumentWord in args:
            argumentCounter = argumentCounter + 1
            checkWord = 0
            for words in item['text'].split(): #split string into words
                word = ""
                for char in words:
                    if char not in punctuations:
                        word = word + char
                if (word == argumentWord): #if word eqauls argument
                    if checkWord == 0:#if word not previously found
                        checkWord = checkWord + 1 #increment
                        wordCounter = wordCounter + 1 #increment
                        
        if (wordCounter == argumentCounter): #if equal add to list
            listofTweets.append(item)
    
    return listofTweets #return new list
            
                
            
            
        
                    
                    