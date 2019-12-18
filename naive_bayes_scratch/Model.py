# MARK:- Libs
import re
from collections import defaultdict
from NaiveBayes import NaiveBayes
import io
import json
import os
from Support import Support

# MARK:- Saving model


class Model:

    # TO-DO: constructor
    def __init__(self, classifier, name):
        """
        create model to contain all detectors and classifiers
        """
        self.classifier = classifier
        self.name = name

    def save(self):
        """
        save current model to file in JSON format
        """

        i = 0
        for ent in self.classifier:
            # extract parameters
            json_part = {}
            cates_info = {}
            json_part["classes"] = ent.classes.tolist()
            oriDic = sorted(ent.cates_info[0][0].items(
            ), key=lambda item: item[1], reverse=True)
            myDic = {}
            for k, v in oriDic:
                if re.match(r'[-@_!#$%^&*()<>?/\|}{~:,.+=\[\]\\\'-;"`]', k):
                    pass
                else:
                    myDic[k] = v
            cates_info[0] = myDic
            cates_info[1] = ent.cates_info[0][1]
            cates_info[2] = ent.cates_info[0][2]
            # save to json model
            json_part["cates_info"] = cates_info
            parsed_json = json.dumps(
                json_part, indent=4, sort_keys=True, ensure_ascii=False)
            os.mkdir(self.name)
            # write to file
            file = io.open(self.name + "/model_" + self.name +
                           "_" + str(i) + ".json", "w", encoding='utf-8')
            file.write(parsed_json)
            file.close()
            i += 1
