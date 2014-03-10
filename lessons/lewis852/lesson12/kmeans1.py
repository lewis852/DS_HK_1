# load modules
from sklearn import cluster, datasets
from sklean.metrics import silhoutte_score
from numpy import random
import pandas as pd
from pandas import read_csv, DataFrame
from pandas import DataFrame, concat
from matplotlib import pyplot as plt
random.seed(1)


train = pd.read_csv('/Users/Lewis/Documents/Datascience/DS_HK_1/lessons/lewis852/lesson10/lemon_training.csv')
test = pd.read_csv('/Users/Lewis/Documents/Datascience/DS_HK_1/lessons/lewis852/lesson10/lemon_test.csv')

cls = cluster.k_means(test, 4)
sil = metrics.silhoutte_score














