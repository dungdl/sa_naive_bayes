from NaiveBayes import NaiveBayes
from sklearn.datasets import fetch_20newsgroups
import numpy as np

categories = ['alt.atheism', 'soc.religion.christian',
              'comp.graphics', 'sci.med']
newsgroups_train = fetch_20newsgroups(subset='train', categories=categories)

train_data = newsgroups_train.data  # getting all training examples
train_labels = newsgroups_train.target

print("[Training with fetch_20newsgroups]")
nb = NaiveBayes(np.unique(train_labels))  # instantiate a NB class object
print("---------------- Training In Progress --------------------")

# start training by calling the train function
nb.cross_validation(train_data, train_labels)
print('----------------- Training Completed ---------------------')

newsgroups_test = fetch_20newsgroups(
    subset='test', categories=categories)  # loading test data
test_data = newsgroups_test.data  # get test set examples
test_labels = newsgroups_test.target  # get test set labels

# Output : Number of Test Examples:  1502
print("Number of Test Examples: ", len(test_data))
print("Number of Test Labels: ", len(test_labels))

pclasses = nb.test(test_data)  # get predcitions for test set

# check how many predcitions actually match original test labels
test_acc = np.sum(pclasses == test_labels)/float(test_labels.shape[0])

print("Test Set Examples: ", test_labels.shape[0])
print("Test Set Accuracy: ", test_acc*100, "%")
