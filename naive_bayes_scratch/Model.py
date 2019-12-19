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
        os.mkdir(self.name)
        i = 0
        for ent in self.classifier:
            # extract parameters
            json_part = {}
            cates_info = {}
            json_part["classes"] = ent.classes.tolist()
            cates_info = {}
            for cate_index, cate in enumerate(ent.classes):
                cate_part = {}
                # get total count of test token, +1 as applying Laplace smoothing
                oriDic = sorted(ent.cates_info[cate_index][0].items(
                ), key=lambda item: item[1], reverse=True)
                myDic = {}
                for k, v in oriDic:
                    if re.match(r'[-@_!#$%^&*()<>?/\|}{~:,.+=\[\]\\\'-;"`]', k):
                        pass
                    else:
                        myDic[k] = v
                cate_part[0] = myDic
                cate_part[1] = ent.cates_info[cate_index][1]
                cate_part[2] = ent.cates_info[cate_index][2]
                cates_info[cate_index] = cate_part

            # save to json model
            json_part["cates_info"] = cates_info
            parsed_json = json.dumps(
                json_part, indent=4, sort_keys=True, ensure_ascii=False)
            
            # write to file
            file = io.open(self.name + "/model_" + self.name +
                           "_" + str(i) + ".json", "w", encoding='utf-8')
            file.write(parsed_json)
            file.close()
            i += 1
