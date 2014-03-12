from pandas import DataFrame
from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

pca = PCA()

pca.fit(iris.data, iris.target)

variance = pca.explained_variance_ratio_

# readable variance rescales the best component to 1
readable_variance = variance * (1/variance[0])
plt.plot(range(4), readable_variance)
plt.show()
















