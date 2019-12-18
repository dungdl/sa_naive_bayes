# MARK:- Libs
import numpy as np
import json
from NaiveBayes import NaiveBayes
from Prediction import Model


class EntityLabel:

    def __init__(self):
        (self.ori_data, self.label_sets) = self.__readfile('train.json')
        self.classifiers = []

        switcher = [
            "Training Restaurant",
            "Training Food",
            "Training Drink",
            "Training Ambience",
            "Training Service",
            "Training Location"
        ]

        for i in range(0, 6):
            print(switcher[i])

            self.ori_labels = self.label_sets[i]

            print("Number of Train Examples: ", len(self.ori_data))
            print("Number of Train Labels: ", len(self.ori_labels))

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

    def __readfile(self, filename):
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

            for i in range(0, 6):
                temp = []
                for tag in tags:
                    temp.append(self.__labeling_entity(tag, i))
                labels.append(temp)

        return (comments, labels)

    def train(self):
        print("[Training Entity Classifier with VLSP 2018]")
        # instantiate a NB class object
        self.nb = NaiveBayes(np.unique(self.ori_labels))
        print("---------------- Training In Progress --------------------")

        # start training by calling the train function
        self.nb.cross_validation(self.ori_data, self.ori_labels)
        self.classifiers.append(self.nb)
        print('----------------- Training Completed ---------------------')

entLabel = EntityLabel()
entLabel.train()
model = Model(entLabel.classifiers, "entity")
model.save()