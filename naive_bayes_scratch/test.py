import json
import numpy as np
from NaiveBayes import NaiveBayes

def test_model(model):
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
        print (nb.test("dev.json"))

# Test Entity
for i in range (0,6):
    test_model("ent/model_ent_" + str(i) + ".json")
# Test Attribute
for i in range (0,12):
    test_model("attr/model_attr_" + str(i) + ".json")
# Test Polar
for i in range (0,12):
    test_model("pol/model_pol_" + str(i) + ".json")