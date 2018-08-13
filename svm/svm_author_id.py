#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

class Timer(object):
    def __init__(self, name=""):
        self.name = name
        self.start = None

    def __enter__(self):
        self.start = time()

    def __exit__(self, type, value, traceback):
        end = time()
        print('{} took {}s'.format(self.name, end-self.start))

clf = SVC(kernel="rbf", C=10000)

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

with Timer("Training"):
    clf.fit(features_train, labels_train)

with Timer("Testing"):
    pred = clf.predict(features_test)

print("accuracy: {:.4f}".format(accuracy_score(labels_test, pred)))

print(sum(pred))

#########################################################

