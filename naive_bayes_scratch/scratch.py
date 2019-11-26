import numpy as np
import json
import time
import re


# MARK:- Get content from json data file
def readfile(filename):
    with open(filename, encoding='utf-8') as json_file:
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

    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
        "+", flags=re.UNICODE)

    emoji_pattern.sub(r'', str)

    words = re.split(' ', str)

    # regex to detect special characters:
    special_regex = re.compile(r'[^\\p{L}\\s]')
    max = len(words) - 1
    for i in range(0, max):
        words[i] = re.sub('[^\w\s]+', '', words[i], flags=re.IGNORECASE)
        if re.match(r'\w', words[i]):
            words[i] = re.sub(
                '[-@_!#$%^&*()<>?/\|}{~:]', ' ', words[i], flags=re.IGNORECASE)
        else:
            words[i] = ''
    # clean string:
    cleaned_str = ' '.join(word for word in words)
    cleaned_str = re.sub('(\s+)', ' ', cleaned_str)
    cleaned_str = cleaned_str.lower()

    return cleaned_str


# MARK:- start training data
train_data = readfile('train.json')

for i in range(1, 10):
    # print(train_data[i])
    print(preprocessing_string(train_data[i]))
    print("----------------")
