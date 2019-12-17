# MARK:- Libs
import numpy as np
import json
import re
import time
from NaiveBayes import NaiveBayes


# MARK:- support function


def test(nb):
    """
    Test accuracy of provided Naive Bayes classifier
    """
    # start testing with test function
    (test_data, labels_set) = readfile('dev.json')
    test_labels = labels_set[0]

    print("Number of Test Examples: ", len(test_data))
    print("Number of Test Labels: ", len(test_labels))

    pclasses = nb.test(test_data)  # get predictions for test set

    # check how many predictions actually match original test labels
    test_acc = np.sum(pclasses == test_labels)/float(len(test_labels))
    print("Test Set Accuracy: ", test_acc*100, "%")

def predict(nb):
    """
    Predict a sample
    """
    (test_data, labels_set) = readfile('dev.json')
    test_labels = labels_set[0]

    print("Number of Test Examples: ", len(test_data))
    print("Number of Test Labels: ", len(test_labels))

    for i in range (100):
        prediction = nb.predict(test_data[i])
        print("====================")
        print(test_data[i])
        print(test_labels[i])
        print(prediction)
        print("=========^^^========")
        time.sleep(2)


def dev(nb, dev_data, dev_label):
    """
    Development test
    """
    # start testing with test function

    print("Number of Dev Examples: ", len(dev_data))
    print("Number of Dev Labels: ", len(dev_label))

    pclasses = nb.test(dev_data)  # get predictions for test set

    # check how many predictions actually match original test labels
    test_acc = np.sum(pclasses == dev_label)/float(len(dev_label))
    print("Dev Set Accuracy: ", test_acc*100, "%")


def labeling_entity(tag, index):
    """
    Label each review based on defined entity
    """
    switcher = [
        "RESTAURANT",
        "FOOD",
        "DRINKS",
        "AMBIENCE",
        "SERVICE",
        "LOCATION"
    ]
    return 1 if switcher[index] in tag.keys() else 0


def cross_validation(nb, ori_data, ori_labels):
    """
    Cross validation within the given dataset
    """
    min_range = 0
    indexer = len(ori_labels) // 10
    max_range = indexer
    for i in range(1):
        if min_range == 0:
            train_data = ori_data[max_range:]
            train_labels = ori_labels[max_range:]

            dev_data = ori_data[: max_range]
            dev_labels = ori_labels[: max_range]
        else:
            if max_range > len(ori_data):
                train_data = ori_data[0: min_range]
                train_labels = ori_labels[0: min_range]

                dev_data = ori_data[min_range:]
                dev_labels = ori_labels[min_range:]

            else:
                train_data = ori_data[0: min_range] + ori_data[max_range:]
                train_labels = ori_labels[0:min_range] + ori_labels[max_range:]

                dev_data = ori_data[min_range: max_range]
                dev_labels = ori_labels[min_range: max_range]

        nb.train(train_data, train_labels)
        dev(nb, dev_data, dev_labels)

        min_range += indexer
        max_range += indexer

        if (min_range >= len(ori_labels)):
            print(min_range)
            print(len(ori_labels))
            print("out of labels")
            break


def readfile(filename):
    """
    Get content from json data file
    """
    with open(filename, encoding='utf-8') as json_file:
        reviews = json.load(json_file)
        comments = []
        labels = []
        tags = []
        for rev in reviews:
            comments.append(rev['comment'])
            tags.append(rev['tags'])

        for i in range(0, 5):
            temp = []
            for tag in tags:
                temp.append(labeling_entity(tag, i))
            labels.append(temp)

    return (comments, labels)


# MARK:- Main script
(ori_data, label_sets) = readfile('train.json')
classifiers = []

for i in range(0, 1):
    if (i == 0):
        print("Training Restaurant")
    elif (i == 1):
        print("Training Food")
    elif (i == 2):
        print("Training Drink")
    elif (i == 3):
        print("Training Ambience")
    elif (i == 4):
        print("Training Service")
    elif (i == 5):
        print("Training Location")

    ori_labels = label_sets[i]

    print("Number of Train Examples: ", len(ori_data))
    print("Number of Train Labels: ", len(ori_labels))

    print("[Training with VLSP 2018]")
    nb = NaiveBayes(np.unique(ori_labels))  # instantiate a NB class object
    print("---------------- Training In Progress --------------------")

    # start training by calling the train function
    cross_validation(nb, ori_data, ori_labels)
    classifiers.append(nb)
    print('----------------- Training Completed ---------------------')

import io, json 

ent = classifiers[0]
temp = {}
t = {}
temp["classes"] = ent.classes.tolist()
oriDic = sorted(ent.cates_info[0][0].items(), key=lambda item: item[1], reverse=True)
myDic = {}
for k,v in oriDic:
    myDic[k] = v
t["dict"] = myDic
t["pd"] = ent.cates_info[0][1]
t["total"] = ent.cates_info[0][2]

temp["cates_info"] = t
# print(type(temp["classes"]))
parsed_json = json.dumps(temp, indent=4, sort_keys=True, ensure_ascii=False)

file = io.open("test.json", "w", encoding='utf-8')
file.write(parsed_json)
file.close()