# MARK:- Libsfrom NaiveBayes import NaiveBayes
import numpy as np
import json
import time
import re
import pprint
from NaiveBayes import NaiveBayes
group_train = []

# MARK:- support function


def test(nb):
    # start testing with test function
    (test_data, labels_set) = readfile('dev.json')
    test_labels = labels_set[0]

    print("Number of Test Examples: ", len(test_data))
    print("Number of Test Labels: ", len(test_labels))

    pclasses = nb.test(test_data)  # get predictions for test set

    # check how many predictions actually match original test labels
    test_acc = np.sum(pclasses == test_labels)/float(len(test_labels))
    print("Test Set Accuracy: ", test_acc*100, "%")


def dev(nb, dev_data, dev_label):
    # start testing with test function

    print("Number of Dev Examples: ", len(dev_data))
    print("Number of Dev Labels: ", len(dev_label))

    pclasses = nb.test(dev_data)  # get predictions for test set

    # check how many predictions actually match original test labels
    test_acc = np.sum(pclasses == dev_label)/float(len(dev_label))
    print("Dev Set Accuracy: ", test_acc*100, "%")

# label each review based on defined entity


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

        # pprint.pprint(tags[:3])

        for i in range(0, 5):
            temp = []
            for tag in tags:
                temp.append(labeling_entity(tag, i))
            labels.append(temp)

    return (comments, labels)


# MARK:- start training data
(ori_data, label_sets) = readfile('train.json')

ori_labels = label_sets[0]

print("Number of Train Examples: ", len(ori_data))
print("Number of Train Labels: ", len(ori_labels))

print("[Training with VLSP 2018]")
nb = NaiveBayes(np.unique(ori_labels))  # instantiate a NB class object
print("---------------- Training In Progress --------------------")

# start training by calling the train function
min_range = 0
indexer = len(ori_labels) // 10
for i in range(10):
    if min_range == 0:
        train_data = ori_data[indexer:]
        train_labels = ori_labels[indexer:]

        dev_data = ori_data[: indexer]
        dev_labels = ori_labels[: indexer]
    else:
        if indexer > len(ori_data):
            train_data = ori_data[0: min_range]
            train_labels = ori_labels[0: min_range]

            dev_data = ori_data[min_range:]
            dev_labels = ori_labels[min_range:]

        else:
            train_data = ori_data[0: min_range] + ori_data[indexer:]
            train_labels = ori_labels[0:min_range] + ori_labels[indexer:]

            dev_data = ori_data[min_range : indexer]
            dev_labels = ori_labels[min_range: indexer]

    nb.train(train_data, train_labels)
    dev(nb, dev_data, dev_labels)

    min_range = indexer
    indexer += indexer
    
    if (min_range >= len(ori_labels)):
        break


print('----------------- Training Completed ---------------------')


test(nb)
