import sys
sys.path.append("..")
from regex.read_restaurant import DataPreprocess
from naive_bayes_scratch.NaiveBayes import preprocessing_string

import collections, re
import pprint

class GenerateStopwords:

    # Init processer
    def __init__ (self):
        self.__processer = DataPreprocess()
        self.__delimiter = "#[0-9]+"

    # Set the resource 
    def setResource(self, resource):
        self.__input = self.__processer.readData(resource)
    
    def generateBagOfWords(self):
        # init empty bag
        bagOfWords = []

        # get first line
        line = self.__input.readline()

        while line:
            x = re.search(self.__delimiter, line)
            if x:
                number = x.string
                content = self.__input.readline()

                cleaned_line = preprocessing_string(content)

                # count frequency of cleaned line
                # then append the counter to bag
                bagOfWords.append(collections.Counter(re.findall(r'\w+', cleaned_line)))
            # get to next line
            line = self.__input.readline()
        
        # init empty counter
        sumBag = collections.Counter()
        
        # merge all the counter in array bagOfWords
        for bow in bagOfWords:
            sumBag += bow

        # sort ascending of most frequency word
        self.__bagOfWords = collections.OrderedDict(sumBag.most_common())

    def getBagOfWords(self):
        return self.__bagOfWords
    
    # write bagOfWords to file (for testing)
    def getBagOfWordsToFile(self, destination):
        output = ""
        for key, value in self.__bagOfWords.items():
            output += key + " : " + str(value) + "\n"

        self.__processer.writeData(destination, output)

    # generate stopword list
    # get top a to b of frequency in bagOfWords
    def generateStopWords(self, a, b):
        stopWords = []
        i = 1
        for key, value in self.__bagOfWords.items():
            if i >= b + 1:
                break

            if i > a and i < b + 1:
                stopWords.append(key)
            i += 1

        self.__stopWords = stopWords

    def getStopWords(self):
        return self.__stopWords

    # write stop word list to file
    def getStopWordsToFile(self, destination):
        output = ""
        for value in self.__stopWords:
            output += value + "\n"

        self.__processer.writeData(destination, output)

    

generator = GenerateStopwords()
generator.setResource("data.txt")
generator.generateBagOfWords()

# generator.getBagOfWordsToFile("bagOfWords.txt")

generator.generateStopWords(10, 100)
generator.getStopWordsToFile("stopWords.txt")