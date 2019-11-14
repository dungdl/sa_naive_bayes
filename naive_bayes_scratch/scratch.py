import numpy as np
import json
import time
import re


# MARK:- Get content from json data file
def readfile(filename):
    with open(filename, encoding='utf8') as json_file:
        reviews = json.load(json_file)
        comments = []
        labels = []
        tags = []
        for rev in reviews:
            comments.append(rev['comment'])
            tags.append(rev['tags'])
    return comments


def preprocessing_string(str):
    # get all words from input string as space is the delimiter
    words = re.split(' ', str)

    # regex to detect special characters:
    special_regex = re.compile('[-@_!#$%^&*()<>?/\|}{~:]')
    for word in words:
        if special_regex.search(word):
            if re.match(r'\w', word):
                word = re.sub('[^a-z]', ' ', str, flags=re.IGNORECASE)
            else:
                words.remove(word)
    # clean string:
    cleaned_str = ' '.join(word for word in words)

    return cleaned_str


# MARK:- start training data
train_data = readfile('train.json')

for i in range(1, 4):
    # print(train_data[i])
    print(preprocessing_string(train_data[i]))
    print("----------------")
