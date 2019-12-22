# MARK:- Libs
import numpy as np
import json
from NaiveBayes import NaiveBayes
from Model import Model

# MARK:- training class


class EntityLabel:

    def __init__(self, fileName):
        (self.ori_data, self.label_sets) = self.readfile(
            fileName)  # get data from file
        self.classifiers = []
        # save original labels as a list
        

    # MARK:- labeling

    def __labeling_entity(self, tag, index):
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

    # MARK:- support functions
    def readfile(self, filename):
        """
        return comments and relative tags as correspond lists
        """
        with open(filename, encoding='utf-8') as json_file:
            reviews = json.load(json_file)
            comments = []
            labels = []
            tags = []
            for rev in reviews:
                comments.append(rev['comment'])
                tags.append(rev['tags'])

            for i in range(0, 6):
                temp = []
                for tag in tags:
                    temp.append(self.__labeling_entity(tag, i))
                labels.append(temp)

        return (comments, labels)

    # MARK:- training session
    def train(self):
        """
        training the Entity Classifier
        """
        for i in range(0, 6):
            ori_labels = self.label_sets[i]
            
            print("[Training Entity Classifier with VLSP 2018]")
            # instantiate a NB class object
            self.nb = NaiveBayes(np.unique(ori_labels))
            print("---------------- Training In Progress --------------------")

            # start training by calling the train function
            self.nb.cross_validation(self.ori_data, ori_labels)
            self.classifiers.append(self.nb)
            print('----------------- Training Completed ---------------------')
