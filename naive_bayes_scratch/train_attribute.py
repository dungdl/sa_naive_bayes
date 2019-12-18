# MARK:- Libs
import numpy as np
import json
import time
from NaiveBayes import NaiveBayes
from Support import Support

# MARK:- labeling functions
class AttributeLabel:

    def __init__(self):
        # MARK:- Main scripts
        (self.comments, tags) = self.__readfile('train.json')  # get data from input file
        self.label = []
        # # Entity Labeling
        (e0_generals, e0_prices, e0_miscels) = self.__e0_labeling(tags)
        (e1_prices, e1_quaity, e1_sno) = self.__e1_labeling(tags)
        (e2_prices, e2_quaity, e2_sno) = self.__e2_labeling(tags)
        e3general_labels = self.__e3_labeling(tags)
        e4general_labels = self.__e4_labeling(tags)
        e5general_labels = self.__e5_labeling(tags)

        # # MARK:- Training session

        self.label = [
            e0_generals, e0_prices, e0_miscels,
            e1_prices, e1_quaity, e1_sno,
            e2_prices, e2_quaity, e2_sno,
            e3general_labels,
            e4general_labels,
            e5general_labels
        ]

    def __labeling_entity(self, tag, index):
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


    def __general_labeler(self, attr):
        """
        label 1 if attribute is GENERAL and 0 otherwise
        """
        key = "GENERAL"
        return 1 if key in attr else 0


    def __prices_labeler(self, attr):
        """
        label 1 if attribute is PRICES and 0 otherwise
        """
        key = "PRICES"
        return 1 if key in attr else 0


    def __quality_labeler(self, attr):
        """
        label 1 if attribute is QUALITY and 0 otherwise
        """
        key = "QUALITY"
        return 1 if key in attr else 0


    def __style_labeler(self, attr):
        """
        label 1 if attribute is STYLE&OPTIONS and 0 otherwise
        """
        key = "STYLE&OPTIONS"
        return 1 if key in attr else 0


    def __mis_labeler(self, attr):
        """
        label 1 if attribute is MISCELLANEOUS and 0 otherwise
        """
        key = "MISCELLANEOUS"
        return 1 if key in attr else 0

    # TO-DO:- labeling attributes in each entity


    def __e0_labeling(self, tags):
        """
        return labels for GENERAL, PRICES and MISCELLANEOUS in Entity 0, respectively
        """
        general_labels = []
        prices_labels = []
        mis_labels = []
        for i in range(len(tags)):
            tag = tags[i]
            entity = self.__labeling_entity(tag, 0)

            if (entity != 1):
                # means that this comment doesn't mentions Entity 0
                general_labels.append(0)
                prices_labels.append(0)
                mis_labels.append(0)
            else:
                # if it does, identify the mentioned attributes of Entity 0
                name_tag = tag["RESTAURANT"]
                general_labels.append(self.__general_labeler(name_tag))
                prices_labels.append(self.__prices_labeler(name_tag))
                mis_labels.append(self.__mis_labeler(name_tag))

        return (general_labels, prices_labels, mis_labels)


    def __e1_labeling(self, tags):
        """
        return labels for PRICES, QUALITY and STYLE&OPTIONS in Entity 1, respectively
        """
        prices_labels = []
        quality_labels = []
        style_labels = []
        for i in range(len(tags)):
            tag = tags[i]
            entity = self.__labeling_entity(tag, 1)

            if (entity != 1):
                # means that this comment doesn't mentions Entity 1
                prices_labels.append(0)
                quality_labels.append(0)
                style_labels.append(0)
            else:
                # if it does, identify the mentioned attributes of Entity 1
                name_tag = tag["FOOD"]
                prices_labels.append(self.__prices_labeler(name_tag))
                quality_labels.append(self.__quality_labeler(name_tag))
                style_labels.append(self.__style_labeler(name_tag))

        return (prices_labels, quality_labels, style_labels)


    def __e2_labeling(self, tags):
        """
        return labels for PRICES, QUALITY and STYLE&OPTIONS in Entity 2, respectively
        """
        prices_labels = []
        quality_labels = []
        style_labels = []
        for i in range(len(tags)):
            tag = tags[i]
            entity = self.__labeling_entity(tag, 2)

            if (entity != 1):
                # means that this comment doesn't mentions Entity 2
                prices_labels.append(0)
                quality_labels.append(0)
                style_labels.append(0)
            else:
                # if it does, identify the mentioned attributes of Entity 2
                name_tag = tag["DRINKS"]
                prices_labels.append(self.__prices_labeler(name_tag))
                quality_labels.append(self.__quality_labeler(name_tag))
                style_labels.append(self.__style_labeler(name_tag))

        return (prices_labels, quality_labels, style_labels)


    def __e3_labeling(self, tags):
        """
        return labels for GENERAL in Entity 3
        """
        general_labels = []
        for i in range(len(tags)):
            tag = tags[i]
            entity = self.__labeling_entity(tag, 3)

            if (entity != 1):
                # means that this comment doesn't mentions Entity 3
                general_labels.append(0)
            else:
                # if it does, identify the mentioned attributes of Entity 3
                name_tag = tag["AMBIENCE"]
                general_labels.append(self.__general_labeler(name_tag))

        return general_labels


    def __e4_labeling(self, tags):
        """
        return labels for GENERAL in Entity 4
        """
        general_labels = []
        for i in range(len(tags)):
            tag = tags[i]
            entity = self.__labeling_entity(tag, 4)

            if (entity != 1):
                # means that this comment doesn't mentions Entity 4
                general_labels.append(0)
            else:
                # if it does, identify the mentioned attributes of Entity 4
                name_tag = tag["SERVICE"]
                general_labels.append(self.__general_labeler(name_tag))

        return general_labels


    def __e5_labeling(self, tags):
        """
        return labels for GENERAL in Entity 5
        """
        general_labels = []
        for i in range(len(tags)):
            tag = tags[i]
            entity = self.__labeling_entity(tag, 5)

            if (entity != 1):
                # means that this comment doesn't mentions Entity 5
                general_labels.append(0)
            else:
                # if it does, identify the mentioned attributes of Entity 5
                name_tag = tag["LOCATION"]
                general_labels.append(self.__general_labeler(name_tag))

        return general_labels

    # MARK:- support functions


    def __readfile(self, filename):
        with open(filename, encoding='utf-8') as json_file:
            reviews = json.load(json_file)
            comments = []
            tags = []
            for rev in reviews:
                comments.append(rev['comment'])
                tags.append(rev['tags'])

        return (comments, tags)

    def train(self):
        self.classifiers = []

        print("[Training Attribute Classifier with VLSP 2018]")
        print("---------------- Training In Progress --------------------")

        for i in range(0, 12):
            print("Training: " + Support.indexToName(i))

            nb = NaiveBayes(np.unique(self.label[i]))

            print('-------- Start Cross Validation ------------')
            nb.cross_validation(self.comments, self.label[i])
            print('-------- End Cross Validation ------------')
            print(len(self.comments))
            print(len(self.label[i]))

            self.classifiers.append(nb)

        print('----------------- Training Completed ---------------------')

attrLabel = AttributeLabel()
attrLabel.train()

from Prediction import Model

model = Model(attrLabel.classifiers, "attr")
model.save()