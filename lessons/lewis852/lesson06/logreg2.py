import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model, feature_selection

baseball = pd.read_csv('/Users/Lewis/Documents/Datascience/DS_HK_1/lessons/lewis852/lesson06/baseball.csv')
baseball = baseball[ ["HR", "RBI", 'R', "G", "SB", "salary", 'height', 'weight', 'yearID'] ]
baseball = baseball.dropna()

sal1 = linear_model.LinearRegression()

HR = [ [x] for x in baseball['HR'].values]
# HR = baseball['HR'].values
RBI = [ [x] for x in baseball['RBI'].values]
R = [ [x] for x in baseball['R'].values]


X = baseball[ ["HR", "RBI", 'R', "G", "SB", 'height', 'weight', 'yearID'] ].values
y = baseball['salary'].values

sal1.fit(X,y)
plt.scatter(HR, y)



