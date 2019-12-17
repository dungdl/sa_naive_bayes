# MARK:- Libs
import numpy as np
import pandas as pd
import re
from collections import defaultdict
from pyvi import ViTokenizer
from NaiveBayes import NaiveBayes

# MARK:- Support methods


def preprocessing_string(str):
    """
    Clean input string with emoji pattern and special characters remover.
    Return a clean string in lower case.
    """
    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
        "+", flags=re.UNICODE)

    emoji_pattern.sub(r'', str)

    # get all words from input string as space is the delimiter
    words = re.split(' ', str)

    # regex to detect special characters:
    max = len(words) - 1
    for i in range(0, max):
        words[i] = re.sub('r[^\w\s]+', '', words[i], flags=re.IGNORECASE)
        if re.match(r'\w', words[i]):
            words[i] = re.sub(
                r'[-@_!#$%^&*()<>?/\|}{~:,.]', ' ', words[i], flags=re.IGNORECASE)
        else:
            words[i] = ''
    # clean string:
    cleaned_str = ' '.join(word for word in words)
    cleaned_str = re.sub('(\s+)', ' ', cleaned_str)
    cleaned_str = cleaned_str.lower()
    cleaned_str = ViTokenizer.tokenize(cleaned_str)
    return cleaned_str


# MARK:- Saving model

class Model:

    # TO-DO: constructor
    def __init__ (self, entity_detectors, attr_detectors, polar_classifiers) :
        """
        create model to contain all detectors and classifiers
        """
        self.entity_detectors = entity_detectors
        self.attr_detectors = attr_detectors
        self.polar_classifiers = polar_classifiers
        self.json_object = []
    
    
    # TO-DO: save entity detectors
    def __save_entity(self):
        temp = {}
        for ent in self.entity_detectors:
            temp[]