# MARK:- Libs
import sys
sys.path.append("//Users//apple//Desktop//Sentiment Analysis//sa_naive_bayes")
from regex.read_restaurant import DataPreprocess
from NaiveBayes import NaiveBayes
import re
import time
import json
import numpy as np


# MARK:- support function

# Labeling
def labeling_entity(entity):
    switcher = {
            "RESTAURANT" : 0,
            "FOOD" : 1,
            "DRINKS" : 2,
            "AMBIENCE" : 3,
            "SERVICE" : 4,
            "LOCATION" : 5
        }
    return switcher.get(entity, 1)

def labeling_attribute(attribute):
    switcher = {
            "GENERAL" : 0,
            "PRICES" : 1,
            "QUALITY" : 2,
            "STYLE&OPTIONS" : 3,
            "MISCELLANEOUS" : 4,
        }
    return switcher.get(attribute, 1)

def labeling_value(value):
    switcher = {
            "neutral" : 0,
            "positive" : 1,
            "negative" : 2
        }
    return switcher.get(value, 1)

# Get content from json data file
def readfile(filename):
    with open(filename, encoding='utf-8') as json_file:
        reviews = json.load(json_file)
        comments = []
        labels = []
        tags = []
        indexs = []
        
        for rev in reviews:
            comments.append(rev['comment'])
            tags.append(rev['tags'])
            indexs.append(rev['index'])

        
        # i = 0
        for i in range(0,len(tags)):
            tag = tags[i]
            print(indexs[i])
            for key in tag.keys():
                print(key)

        #     i += 1
        #     if i > 10:
        #         break


readfile('train.json')
