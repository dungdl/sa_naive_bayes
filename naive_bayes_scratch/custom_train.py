from NaiveBayes import NaiveBayes
import numpy as np

# MARK:- Libs
import json
import re

group_train = []

# MARK:- Get content from json data file
with open('test.json', encoding='utf8') as json_file:
    reviews = json.load(json_file)
    comments = []
    labels = []
    tags = []
    for rev in reviews:
        comments.append(rev['comment'])
        tags.append(rev['tags'])

    for tag in tags:
        positive = 0
        negative = 0
        neutral = 0

        for attr in tag.values():
            for val in list(attr.values()):
                if val == "positive":
                    positive += 1
                if val == "negative":
                    negative += 1
                if val == "neutral":
                    neutral += 1
