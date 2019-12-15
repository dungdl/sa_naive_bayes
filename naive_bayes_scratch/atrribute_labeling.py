# MARK:- Libs
import numpy as np
import json
import time
import re
import pprint
from NaiveBayes import NaiveBayes
from entity_labeling import cross_validation


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

# TO-DO: binary labeling for each attribute


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

# TO-DO:- labeling attributes in each entity


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
        entity = labeling_entity(tag, 2)

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


def e3_labeling(tags):
    """
    return labels for GENERAL in Entity 3
    """
    general_labels = []
    for i in range(len(tags)):
        tag = tags[i]
        entity = labeling_entity(tag, 3)

        if (entity != 1):
            # means that this comment doesn't mentions Entity 3
            general_labels.append(0)
        else:
            # if it does, identify the mentioned attributes of Entity 3
            name_tag = tag["AMBIENCE"]
            general_labels.append(general_labeler(name_tag))

    return general_labels


def e4_labeling(tags):
    """
    return labels for GENERAL in Entity 4
    """
    general_labels = []
    for i in range(len(tags)):
        tag = tags[i]
        entity = labeling_entity(tag, 4)

        if (entity != 1):
            # means that this comment doesn't mentions Entity 4
            general_labels.append(0)
        else:
            # if it does, identify the mentioned attributes of Entity 4
            name_tag = tag["SERVICE"]
            general_labels.append(general_labeler(name_tag))

    return general_labels


def e5_labeling(tags):
    """
    return labels for GENERAL in Entity 5
    """
    general_labels = []
    for i in range(len(tags)):
        tag = tags[i]
        entity = labeling_entity(tag, 5)

        if (entity != 1):
            # means that this comment doesn't mentions Entity 5
            general_labels.append(0)
        else:
            # if it does, identify the mentioned attributes of Entity 5
            name_tag = tag["LOCATION"]
            general_labels.append(general_labeler(name_tag))

    return general_labels

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


# MARK:- Main scripts

(comments, tags, indexs) = readfile('train.json')  # get data from input file
label = []
# # Entity Labeling
(e0_generals, e0_prices, e0_miscels) = e0_labeling(tags)
(e1_prices, e1_quaity, e1_sno) = e1_labeling(tags)
(e2_prices, e2_quaity, e2_sno) = e2_labeling(tags)
e3general_labels = e3_labeling(tags)
e4general_labels = e4_labeling(tags)
e5general_labels = e5_labeling(tags)

# # MARK:- Training session

label = [
    e0_generals, e0_prices, e0_miscels,
    e1_prices, e1_quaity, e1_sno,
    e2_prices, e2_quaity, e2_sno,
    e3general_labels,
    e4general_labels,
    e5general_labels
]


def indexToName(index):
    switcher = {
        0: "RESTAURENT_generals",
        1: "RESTAURENT_prices",
        2: "RESTAURENT_miscels",
        3: "FOOD_prices",
        4: "FOOD_quality",
        5: "FOOD_sno",
        6: "DRINKS_prices",
        7: "DRINKS_quality",
        8: "DRINKS_sno",
        9: "AMBIENCE_generals",
        10: "SERVICE_generals",
        11: "LOCATION_generals"
    }
    return switcher.get(index, 12)


classifiers = []

print("[Training with VLSP 2018]")
print("---------------- Training In Progress --------------------")

for i in range(0, 12):
    print("Training: " + indexToName(i))

    nb = NaiveBayes(np.unique(label[i]))

    print('-------- Start Cross Validation ------------')
    cross_validation(nb, comments, label[i])
    print('-------- End Cross Validation ------------')
    print(len(comments))
    print(len(label[i]))

    classifiers.append(nb)


print('----------------- Training Completed ---------------------')
