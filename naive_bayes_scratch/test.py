import json
import numpy as np
from Support import Support
from NaiveBayes import NaiveBayes
from train_attribute import AttributeLabel
from train_entity import EntityLabel
from train_polarity import PolarLabel

def test(nb, scope, i):
    # start testing with test function
    if (scope == "ent"):
        label = EntityLabel("train.json")
        (test_data, test_labels) = label.readfile('dev.json')
    if (scope == "attr"):
        label = AttributeLabel("dev.json")
        test_data = label.comments
        test_labels = label.label

    if (scope == "pol"):
        label = PolarLabel("dev.json")
        test_data = label.comments
        test_labels = label.label

    print("Number of Test Examples: ", len(test_data))
    print("Number of Test Labels: ", len(test_labels[i]))

    pclasses = nb.test(test_data)  # get predictions for test set

    # check how many predictions actually match original test labels
    test_acc = np.sum(pclasses == test_labels[i])/float(len(test_labels[i]))
    print("Test Set Accuracy: ", test_acc*100, "%")
        


def get_model(model):
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
        return nb
# Test Entity
# for i in range (0,6):
#     print("Testing Entity : " + Support.indexToEntity(i))
#     model = get_model("ent/model_ent_" + str(i) + ".json")
#     test(model, "ent", i)
# # Test Attribute
# for i in range (0,12):
#     print("Testing Attribute : " + Support.indexToName(i))
#     model = get_model("attr/model_attr_" + str(i) + ".json")
#     test(model, "attr", i)
# Test Polar
for i in range (0,12):
    print("Testing Polar : " + Support.indexToName(i))
    model = get_model("pol/model_pol_" + str(i) + ".json")
    test(model, "pol", i)