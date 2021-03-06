# load modules
from sklearn import cluster, metrics. datasets
from sklearn.metrics import silhoutte_score
from numpy import random
from pandas import DataFrame, concat
from matplotlib import pyplot as plt
random.seed(1)

# We are creating four naturally separated data clusters
# Randomrandom gives you a number betweeen zero and one
classone = DataFrame({
    'x' :random.random(20) + 1,
    'y' : random.random(20) + 1,
    'label' : ['r' for i in range(20)]
})
classtwo = DataFrame({
    'x' :random.random(20) + 1,
    'y' : random.random(20) + 3,
    'label' : ['g' for i in range(20)]
})
classthree = DataFrame({
    'x' :random.random(20) + 3,
    'y' : random.random(20) + 1,
    'label' : ['b' for i in range(20)]
})
classfour = DataFrame({
    'x' :random.random(20) + 3,
    'y' : random.random(20) + 3,
    'label' : ['purple' for i in range(20)]
})

# This creates a data frame based on our 4 smaller dataframes we have defined
data = concat([classone, classtwo, classthree, classfour])

plt.scatter(data.x.values, data.y.values, color=list(data.label.values))
plt.title('Really Easy Clusters')
plt.show()

# K is Red, Green, Blue, Purple so 4 clusters = k 
cls = cluster.k_means(data[ ['x', 'y'] ].values, 4)

data['clusters'] = cls[1]

plt.scatter(data.x.values, data.y.values, c=list(data.clusters.values))
plt.title('Clusters Identifed by color')
plt.show()

classfive = DataFrame({
    'x' : random.random(50) * 50 + 100,
    'y' : random.random(50) * 50 + 100,
    'label' : ['orange' for i in range(50)]
})
data = concat([data, classfive])
cls = cluster.k_means(data[ ['x', 'y'] ].values, 5)
data['clusters'] = cls[1]

plt.scatter(data.x.values, data.y.values, c=list(data.clusters.values))
plt.title('Clusters Identifed by color')
plt.show()

#import data sets at top for Iris Data
iris = datasets.load_iris()
cls = cluster.k_means(iris.data, 3)

plt.subplot(211)
plt.scatter(iris.data[:,:1], iris.data[:, 1:2], cmap=plt.cm.jet, c=iris.target)
plt.subplot(212)
plt.scatter(iris.data[:,:1], iris.data[:, 1:2], cmap=plt.cm.jet, c=list(cls[1]))
plt.show()

# silhouette score being updated in the wiki. 
sil = silhoutte_score(iris.data,cls[1])


















