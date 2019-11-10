# MARK:- Libs
import pandas as pd
import numpy as np
from collections import defaultdict
import re

# MARK:- Preprocessing data


def preprocessing_string(str):

    # replace every characters except alphabet with a space
    cleaned_str = re.sub('[^a-z\s]+', ' ', str, flags=re.IGNORECASE)
    # merge multiple space into one
    cleaned_str = re.sub('(\s+)', ' ', cleaned_str)
    # lower case all characters
    cleaned_str = cleaned_str.lower()

    return cleaned_str
