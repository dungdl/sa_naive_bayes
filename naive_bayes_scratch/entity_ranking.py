# MARK:- Libs
import pprint
import collections
import numpy as np
import json
import time
import re
import sys
sys.path.append("..")

from NaiveBayes import NaiveBayes
from regex.read_restaurant import DataPreprocess



# MARK:- support function

# Labeling
def labeling_entity(entity):
    switcher = {
        "RESTAURANT": 1,
        "FOOD": 2,
        "DRINKS": 3,
        "AMBIENCE": 4,
        "SERVICE": 5,
        "LOCATION": 6
    }
    return switcher.get(entity, 1)


def labeling_attribute(attribute):
    switcher = {
        "GENERAL": 1,
        "PRICES": 2,
        "QUALITY": 3,
        "STYLE&OPTIONS": 4,
        "MISCELLANEOUS": 5,
    }
    return switcher.get(attribute, 1)


def labeling_value(value):
    switcher = {
        "neutral": 1,
        "positive": 2,
        "negative": 3
    }
    return switcher.get(value, 1)

# Get content from json data file


def rankEntities(filename):
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
        for i in range(0, len(tags)):
            tag = tags[i]
            # print(indexs[i])
            for key_entity, value_entity in tag.items():
                label = labeling_entity(key_entity) * 100
                for key_attr, value_attr in value_entity.items():
                    label += labeling_attribute(key_attr) * \
                        10 + labeling_value(value_attr)
                    # print (label)
                    labels.append(label)

        frequency = collections.Counter(labels)
        frequency = collections.OrderedDict(frequency.most_common())

        # print (frequency)
        print(len(frequency))
        # pprint.pprint(frequency)


rankEntities('train.json')

#--------------------------------------------------#
