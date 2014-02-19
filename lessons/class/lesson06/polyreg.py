import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

mammals = pd.read_csv('mammals.csv')
lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()
body = [ [x] for x in mammals['body'].values]
log_body = log_body = [ [x] for x in np.log(mammals['body'].values)]
brain = mammals['brain'].values
log_brain = np.log(mammals['brain'].values)
lm.fit(body, brain)
log_lm.fit(log_body, log_brain)


print lm.intercept_
print log_lm.intercept_
print lm.coef_
print log_lm.intercept_

