# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 19:31:06 2014

@author: RahulKapur
"""
#Rahul Kapur
#rk2749

import tweets as tweet
def main():
    tweetList = tweet.make_tweets("/Users/RahulKapur/Desktop/test.txt")  
    #create list of dictionaries
    tweet.add_sentiment(tweetList, "/Users/RahulKapur/Downloads/sentiments.csv") 
    #add sentiment to dictionaries
    tweetsWithSentiment = tweet.readNewFileWithSentiment("/Users/RahulKapur/Desktop/outputfile.txt")
    #readNewSentiments
    tweetListNew = tweet.tweet_filter(tweetsWithSentiment, "and", "ime", "hi")
    #filter the list according to words
    averageSentiment = tweet.avg_sentiment(tweetListNew)
    #find the average sentiment of filtered list
main()