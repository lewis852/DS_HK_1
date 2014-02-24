# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets, feature_selection

# Download and create a dataset for the beer data
url = 'http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt'
beer = pd.read_csv(url, delimiter="\t")
beer = beer.dropna()

# Define how many neighbours we are going to test for the optimal K
n_neighbors = range(1, 101, 2)
np.random.seed(1234)

def good(x):
  if x > 4.3:
    return 1
  else:
    return 0


X = beer['WR'].apply(good)
y = 







