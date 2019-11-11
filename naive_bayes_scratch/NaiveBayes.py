# MARK:- Libs
import numpy as np
import pandas as pd
from collections import defaultdict
import re

# MARK:- Support methods

# preprocessing data


def preprocessing_string(str):

    # replace every characters except alphabet with a space
    cleaned_str = re.sub('[^a-z\s]+', ' ', str, flags=re.IGNORECASE)
    # merge multiple space into one
    cleaned_str = re.sub('(\s+)', ' ', cleaned_str)
    # lower case all characters
    cleaned_str = cleaned_str.lower()

    return cleaned_str

# MARK:- NB class


class NaiveBayes:

    # TO-DO: constructor
    def __init__(self, num_class):
        # set number of class to NB classifier
        self.classes = num_class

    # TO-DO: init bag of word for the category
    def creatBagOfWord(self, example, dict_index):
        if isinstance(example, np.ndarray):
            example = example[0]
        # count number of word appeared in the example
        for token_word in example.split():
            self.bag_dicts[dict_index][token_word] += 1

    # TO-DO: train the NB classifier
    def train(self, dataset, labels):
        # read input params
        self.examples = dataset
        self.labels = labels
        self.bag_dicts = np.array([defaultdict(lambda: 0)
                                   for index in range(self.classes.shape[0])])

        # only convert to numpy arrays if initially not passed as numpy arrays
        if not isinstance(self.examples, np.ndarray):
            self.examples = np.array(self.examples)
        if not isinstance(self.labels, np.ndarray):
            self.labels = np.array(self.labels)

        # create BoW for each category
        for cate_index, cate in enumerate(self.classes):
            # get all examples of category equal cate
            all_cate_examples = self.examples[self.labels == cate]

            # clean examples
            cleaned_exams = [preprocessing_string(
                cate_exam) for cate_exam in all_cate_examples]
            cleaned_exams = pd.DataFrame(data=cleaned_exams)

            # store this bag of word of the particular category
            np.apply_along_axis(self.creatBagOfWord, 1,
                                cleaned_exams, cate_index)

        # TO-DO: calculate parameters for prior probability of class c - p(c)
        prob_classes = np.empty(self.classes.shape[0])
        words = []
        cate_word_counts = np.empty(self.classes.shape[0])

        for cate_index, cate in enumerate(self.classes):
            # get p(c)
            prob_classes[cate_index] = np.sum(
                self.labels == cate) / float(self.labels.shape[0])

            # get total count of words in each class
            count = list(self.bag_dicts[cate].values())
            cate_word_counts[cate_index] = np.sum(
                np.array(list(self.bag_dicts[cate_index].values()))) + 1

            # get all words of this category
            words = self.bag_dicts[cate_index].keys()

        # build vocabulary set and get size of the set
        self.vocab = np.unique(np.array(words))
        self.vocab_size = self.vocab.shape[0]

        # get p(d) - denominator value
        denominators = np.array([cate_word_counts[cate_index] + self.vocab_size +
                                 1 for cate_index, cate in enumerate(self.classes)])

        # change all category info to tuple format
        self.cates_info = [(self.bag_dicts[cate_index], prob_classes[cate_index],
                            denominators[cate_index]) for cate_index, cate in enumerate(self.classes)]
        self.cates_info = np.array(self.cates_info)

    # TO-DO: calculate the posterior probability of given test example

    def calExProb(self, test_ex):
        likelihood_prob = np.zeros(self.classes.shape[0])

        for cate_index, cate in enumerate(self.classes):
            for test_token in test_ex.split():

                # get total count of test token, +1 as applying Laplace smoothing
                test_token_count = self.cates_info[cate_index][0].get(
                    test_token, 0) + 1

                # get likelihood probability of this test token
                test_token_prob = test_token_count / \
                    float(self.cates_info[cate_index][2])

                # store to the output array, reform to log to save calculating capacity
                likelihood_prob[cate_index] += np.log(test_token_prob)

        # get posterior probability
        post_prob = np.empty(self.classes.shape[0])
        for cate_index, cate in enumerate(self.classes):
            post_prob[cate_index] = likelihood_prob[cate_index] + \
                np.log(self.cates_info[cate_index][1])

        return post_prob

    # TO-DO: estimate the probability of the prediction for given test set
    def test(self, test_set):
        predictions = []

        for ex in test_set:

            # clean the example
            cleaned_exams = preprocessing_string(ex)

            # get posterior probability of every examples in test set
            post_prob = self.calExProb(cleaned_exams)

            predictions.append(self.classes[np.argmax(post_prob)])

        return np.array(predictions)
