 import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

mammals = pd.read_csv('/Users/Lewis/Documents/Datascience/DS_HK_1/lessons/lewis852/lesson05/mammals.csv')
lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()
body = [ [x] for x in mammals['body'].values]
log_body = log_body = [ [x] for x in np.log(mammals['body'].values)]
brain = mammals['brain'].values
log_brain = np.log(mammals['brain'].values)
lm.fit(body, brain)
log_lm.fit(log_body, log_brain)

import matplotlib.pyplot as plt

lm.predict(body)
mammals['predict'] = lm.predict(body)
log_lm.predict(log_body)
mammals['log_predict'] = np.exp(log_lm.predict(log_body))

# Sort by response:
mammals = mammals.sort('brain')
# Sort by prediction:
mammals_log_sort = mammals.sort('log_predict')


plt.scatter(body, mammals_log_brain, c='b', marker='o')

plt.plot(body, lm/predict(body), exp(log_body),np.exp(log_lm.predict(log_body)))
show.plt


print lm.intercept_
print log_lm.intercept_
print lm.coef_
print log_lm.intercept_


#POLYNOMIAL REGRESSION CLASSWORK
mammals['body_squared'] = mammals['body']**2

# Here we are creating another column with the body values squared! 


body_squared = [ [x, y] for x,y in zip(mammals['body'].values, mammals['body_squared'].values)]
# OR
body_squared = [ [x, y] for x,y in zip(mammals['body'].values, (mammals['body'].values)**2]    

ridge = linear_model.Ridge()
ridge.fit(body_squared, brain)

# Where Body Squared is the X matrix with body and body squared as dependent variables. Brain is our Response Vector (the Y) 

((ridge.coef_[1] * mammals['body'])**2) + ((ridge.coef_[0] * mammals['body'])) + ridge.intercept_

ridge.coef_





