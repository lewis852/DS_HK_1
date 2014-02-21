import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import re
re.search('Apple', 'Apple Computer') != None # If this is true, then there was a match!

from sklearn import linear_model
from sklearn import feature_selection

url = 'http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt'
beer = pd.read_csv(url, delimiter="\t")
beer = beer.dropna()

def good(x):
  if x > 4.3:
    return 1
  else:
    return 0

beer['Good'] = beer['WR'].apply(good)

input = beer[ ['Reviews', 'ABV'] ].values
good = beer['Good'].values

logm = linear_model.LogisticRegression()

logm.fit(input, good)
logm.predict(input)
logm.score(input, good)

beer_types = ['Ale', 'Stout', 'IPA', 'Lager']

for t in beer_types: 
	beer[t] = beer['Type'].str.contains(t) * 1

input = beer[['Reviews', 'ABV', 'Ale', 'Stout', 'IPA', 'Lager']].values

fp_value = feature_selection.univariate_selection.f_regression(input, good)

input = beer[['ABV', 'Ale', 'Stout']].values

y = beer['Good'].values

logm.fit(input, y)

logm.fit(input, good)
logm.predict(input)
logm.score(input, good)













