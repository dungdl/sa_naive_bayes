# MARK:- Libs
import numpy as np
import pandas as pd
from collections import defaultdict
from pyvi import ViTokenizer
import re

class Support:

    @staticmethod
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
    @staticmethod
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
