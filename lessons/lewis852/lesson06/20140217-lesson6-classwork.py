import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import feature_selection

cars = pd.read_csv('/Users/Lewis/Documents/Datascience/DS_HK_1/lessons/lewis852/lesson06/cars93.csv')

cars_input = cars._get_numeric_data()



feature_selection.univariate_selection.f_regression(input, response)

