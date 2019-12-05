
from NaiveBayes import NaiveBayes
import sys
sys.path.append("E:\\Computational Linguistics\\Sentiment Analysis\\sa_naive_bayes")
from regex.read_restaurant import DataPreprocess

dp = DataPreprocess()
dp.labeling('data.txt', 'dev.json')
