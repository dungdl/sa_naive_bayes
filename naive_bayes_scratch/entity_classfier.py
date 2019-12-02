# MARK:- Libsfrom NaiveBayes import NaiveBayes
import numpy as np
import json
import time
import re
from NaiveBayes import NaiveBayes

group_train = []

# MARK:- support function

# label each review based on defined entity


def labeling_entity(entity):
    switcher = {
        "RESTAURANT": 0,
        "FOOD": 1,
        "DRINKS": 2,
        "AMBIENCE": 3,
        "SERVICE": 4,
        "LOCATION": 5
    }
    return switcher.get(entity, 1)

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
            print(tag.keys())
            # labels.append(labeling_entity)

    return (comments, labels)


readfile('restaurant.json')
"""
def test(nb):
    # start testing with test function
    (test_data, test_labels) = readfile('dev.json')

    # for i in range(1, 10):
    #     # print(train_data[i])
    #     print(nb.predict(train_data[i]))
    #     print(train_labels[i])
    #     print("----------------")

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
for word in nb.bag_dicts:
    print(word)


#test(nb)
"""