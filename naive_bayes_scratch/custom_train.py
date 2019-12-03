# MARK:- Libs
import sys
sys.path.append("//Users//apple//Desktop//Sentiment Analysis//sa_naive_bayes")
import numpy as np
import json
import time
import re
from NaiveBayes import NaiveBayes
from regex.read_restaurant import DataPreprocess



# MARK:- support function
group_train = []
# get label by comparing individual tags' labels


def max(positive, negative, neutral):
    if positive == negative:
        return 2
    if positive > negative:
        if neutral > positive:
            return 2
        return 1
    if negative > positive:
        if neutral > negative:
            return 2
        return 0


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
            labels.append(max(positive, negative, neutral))
    return (comments, labels)


def test(nb):
    # start testing with test function
    (test_data, test_labels) = readfile('train.json')

    print("Number of Test Examples: ", len(test_data))
    print("Number of Test Labels: ", len(test_labels))

    pclasses = nb.test(test_data)  # get predictions for test set

    # check how many predictions actually match original test labels
    test_acc = np.sum(pclasses == test_labels)/float(len(test_labels))
    print("Test Set Accuracy: ", test_acc*100, "%")


# MARK:- start training data
(train_data, train_labels) = readfile('train.json')

print("Number of Train Examples: ", len(train_data))
print("Number of Train Labels: ", len(train_labels))

print("[Training with VLSP 2018]")
nb = NaiveBayes(np.unique(train_labels))  # instantiate a NB class object
print("---------------- Training In Progress --------------------")

# start training by calling the train function
nb.train(train_data, train_labels)
print('----------------- Training Completed ---------------------')

test(nb)
