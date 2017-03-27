# first iteration of a sentiment analysis
#python first run, unedited. Might not work right-off the bat.

__author__ = "CavHack"

import csv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
import sklearn import cross_validation
from sklearn.metrics import classification_report
import numpy as np
from sklearn.metrics import accuracy_score

#Your first task is explore this directory. There are two sub-directories pos/ for positive texts and neg/ for negative ones.
#Now combine the raw database into a single csv files, “imdb_tr.csv”.
#The csv file should have three columns, "row_number" and “text” and “polarity”.
#The column “text” contains review texts from the aclImdb database and the column “polarity” consists of sentiment labels,
# 1 for positive and 0 for negative.
#An example of "imdb.tr.csv" is provided in the workspace.

def load_file():
    with open('imdb.tr.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=",", quotechars='""')
        reader.next()
        data = []
        target = []
        for row in reader:
            #skip missing data if any.

            if row[0] and row[1]:
                data.append(row[0])
                target.append(row[1])

                return data, target
#preprocess creates the term frequency matrix for the review data sentiment

def preprocess():
    data, target = load_file()
    #http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
    count_vectorizer = CountVectorizer(binary='true')
    data = count_vectorizer.fit_transform(data)
    tfidf_data = TfidfTransformer(use_idf=false).fit_transform(data)

    return tfidf_data

def learn_model(data, target)
    #preparing data for cleavage(split validation. 60/40)
    data_train, data_test, target_train, target_test = cross_validation.train_test_split(data, target, test_size=0.4, random_state=43)
    classifier = BernoulliNB.fit(data_train, target_train)
    predicted = classifier.predict(data_set)
    evaluate_model(target_test, predicted)

#model-eval pass through
def evaluate_model(target_true, target_predicted):
    print classification_report(target_true, target_predicted)
    print "The accuracy score is {:.2%}".format(accuracy_score(target_true, target_predicted))


def main():
    data, target = load_file()
    tf_idf = preprocess()
    learn_model(tf_idf, target)

    main()
