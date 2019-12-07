# MARK:- Libs
import numpy as np
import json
import time
import re
import pprint
from NaiveBayes import NaiveBayes


# MARK:- labeling functions


def labeling_entity(tag, index):
    switcher = [
        "RESTAURANT",
        "FOOD",
        "DRINKS",
        "AMBIENCE",
        "SERVICE",
        "LOCATION"
    ]
    return 1 if switcher[index] in tag.keys() else 0


def general_labeler(attr):
    """
    label 1 if attribute is GENERAL and 0 otherwise
    """
    key = "GENERAL"
    return 1 if key in attr else 0


def prices_labeler(attr):
    """
    label 1 if attribute is PRICES and 0 otherwise
    """
    key = "PRICES"
    return 1 if key in attr else 0


def quality_labeler(attr):
    """
    label 1 if attribute is QUALITY and 0 otherwise
    """
    key = "QUALITY"
    return 1 if key in attr else 0


def style_labeler(attr):
    """
    label 1 if attribute is STYLE&OPTIONS and 0 otherwise
    """
    key = "STYLE&OPTIONS"
    return 1 if key in attr else 0


def mis_labeler(attr):
    """
    label 1 if attribute is MISCELLANEOUS and 0 otherwise
    """
    key = "MISCELLANEOUS"
    return 1 if key in attr else 0


# MARK:- support functions

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

    return (comments, tags, indexs)


def e0_labeling(tags):
    """
    return labels for GENERAL, PRICES and MISCELLANEOUS in Entity 0, respectively
    """
    general_labels = []
    prices_labels = []
    mis_labels = []
    for i in range(len(tags)):
        tag = tags[i]
        entity = labeling_entity(tag, 0)
        
        if (entity != 1):
            # means that this comment doesn't mentions Entity 0
            general_labels.append(0)
            prices_labels.append(0)
            mis_labels.append(0)
        else:
            # if it does, identify the mentioned attributes of Entity 0
            name_tag = tag["RESTAURANT"]
            general_labels.append(general_labeler(name_tag))
            prices_labels.append(prices_labeler(name_tag))
            mis_labels.append(mis_labeler(name_tag))

    return (general_labels, prices_labels, mis_labels)

def e1_labeling(tags):
    """
    return labels for PRICES, QUALITY and STYLE&OPTIONS in Entity 1, respectively
    """
    prices_labels = []
    quality_labels = []
    style_labels = []
    for i in range(len(tags)):
        tag = tags[i]
        entity = labeling_entity(tag, 1)
        
        if (entity != 1):
            # means that this comment doesn't mentions Entity 1
            prices_labels.append(0)
            quality_labels.append(0)
            style_labels.append(0)
        else:
            # if it does, identify the mentioned attributes of Entity 1
            name_tag = tag["FOOD"]
            prices_labels.append(prices_labeler(name_tag))
            quality_labels.append(quality_labeler(name_tag))
            style_labels.append(style_labeler(name_tag))

    return (prices_labels, quality_labels, style_labels)

def e2_labeling(tags):
    """
    return labels for PRICES, QUALITY and STYLE&OPTIONS in Entity 2, respectively
    """
    prices_labels = []
    quality_labels = []
    style_labels = []
    for i in range(len(tags)):
        tag = tags[i]
        entity = labeling_entity(tag, 1)
        
        if (entity != 1):
            # means that this comment doesn't mentions Entity 2
            prices_labels.append(0)
            quality_labels.append(0)
            style_labels.append(0)
        else:
            # if it does, identify the mentioned attributes of Entity 2
            name_tag = tag["DRINKS"]
            prices_labels.append(prices_labeler(name_tag))
            quality_labels.append(quality_labeler(name_tag))
            style_labels.append(style_labeler(name_tag))

    return (prices_labels, quality_labels, style_labels)


# MARK:- Main scripts
(comments, tags, indexs) = readfile('train.json')
(general_labels,  prices_labels, mis_labels) = e1_labeling(tags)
print(len(comments))
print(len(general_labels))
print(len(prices_labels))
print(len(mis_labels))
