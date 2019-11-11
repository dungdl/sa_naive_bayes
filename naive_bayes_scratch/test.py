from NaiveBayes import NaiveBayes
from sklearn.datasets import fetch_20newsgroups

newsgroups_test=fetch_20newsgroups(subset='test',categories=categories) #loading test data
test_data=newsgroups_test.data #get test set examples
test_labels=newsgroups_test.target #get test set labels

print ("Number of Test Examples: ",len(test_data)) # Output : Number of Test Examples:  1502
print ("Number of Test Labels: ",len(test_labels)) # Output : Number of Test Labels:  1502