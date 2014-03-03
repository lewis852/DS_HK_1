
# import libraries required for decision tree analysis in lemon project
from sklearn import datasets, metrics, tree, cross_validation
from matplotlib import pyplot as plt
import pandas as pd
from pandas import read_csv, DataFrame

# identify my car training and test data as dataframe
train = pd.read_csv('/Users/Lewis/Documents/Datascience/DS_HK_1/lessons/lewis852/lesson10/lemon_training.csv')
test = pd.read_csv('/Users/Lewis/Documents/Datascience/DS_HK_1/lessons/lewis852/lesson10/lemon_test.csv')

features = ['VehicleAge','VehYear','VehBCost'] #ignoring 'Make','Model', how do I add them in? 
X = [[x[0],x[1],x[2]] for x in train[features].values]
y = train['IsBadBuy'].values

X_test = test[features].values	

# define y predictive variable

clf = tree.DecisionTreeClassifier()
clf.fit(X, y)
y_pred = clf.predict(X)


print "Number of mislabeled points : %d" % (y != y_pred).sum()
print "Absolutely ridiculously overfit score: %d" % (tree.DecisionTreeClassifier().fit(X,
    y).score(X, y))










