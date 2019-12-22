import json
import numpy as np
from NaiveBayes import NaiveBayes
from Support import Support

def predict_model(model, review):
    """
    load model from json file then call NaiveBayes.test() to test
    """
    with open(model, encoding='utf-8') as json_file:
        data = json.load(json_file)
        classes = np.asarray(data["classes"])
        cates_info = data["cates_info"]
        cates_info = {int(k): v for k,v in cates_info.items()}
        for cate_index, cate in enumerate(classes):
            cates_info[cate_index] = {int(k): v for k,v in cates_info[cate_index].items()}
        nb = NaiveBayes(classes)
        nb.cates_info = cates_info
        return nb.predict(review)

def get_attr(entity):
    """
    return attribute of para entity
    """
    switcher = {
            0: [0, 1, 2],
            1: [3, 4, 5],
            2: [6, 7, 8],
            3: [9],
            4: [10],
            5: [11],
        }
    return switcher.get(entity, 6)



import sys

def run(review):
    review = str(review)
    result = ""
    for i in range(0, 6):
        if predict_model("ent/model_ent_" + str(i) + ".json", review) == 1:
            attrs = get_attr(i)
            for attr_index, attr in enumerate(attrs):
                if predict_model("attr/model_attr_" + str(attr) + ".json", review) == 1:
                    polar = predict_model("pol/model_pol_" + str(attr) + ".json", review)
                    if (polar != 0):
                        result += str(Support.indexToName(attr)) + " : " + Support.indexToPolar(polar) + "\n"
    print(result)
    return result
if __name__ == '__main__':
    run(sys.argv)

