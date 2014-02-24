import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets, feature_selection

# Various variables we'll need to set intially.
# 1 is the start number, 2 is the step - so we don't get even number of neighbours
n_neighbors = range(1, 101, 2)
np.random.seed(1234)

# Load in the data and seperate the class labels and input data
iris = datasets.load_iris()
X = iris.data[:, :4]
y = iris.target

# Create the training (and test) set using the rng in numpy
n = len(y) * .7
ind = np.hstack((np.ones(n, dtype=np.bool), np.zeros(len(y) - n, dtype=np.bool)))
np.random.shuffle(ind)

# Assigning our TRAINING and TEST datasets. 
X_train, X_test = X[ind], X[ind == False]
y_train, y_test = y[ind], y[ind == False]

# Or more concisely
idx = np.random.uniform(0, 1, len(X)) <= 0.3
X1_train, X1_test = X[idx], X[idx==False]
y1_train, y1_test = y[idx], y[idx==False]

# Loop through each neighbors value from 1 to 100 and append
# the scores
scores = []
for n in n_neighbors:
    clf = neighbors.KNeighborsClassifier(n, weights='uniform')
    clf.fit(X_train, y_train)    
    scores.append(clf.score(X_test, y_test))

plt.plot(n_neighbors, scores)
plt.show()

results = []
for n in [7,9,11,13,15]

scores = []
for k in range(5):
    np.random.shuffle(ind)
    X_train, X_test = X[ind], X[ind == False]
    y_train, y_test = y[ind], y[ind == False]
    clf = neighbors.KNeighborsClassifier(n, weights='uniform')
    clf.fit(X_train, y_train)
    scores.append(clf.score(X_test, y_test))

[np.mean(x) for x in results]


print scores
print np.mean(scores)
print results

# Below returns highest signifiance for features 2 and 3
# (remember, Python uses index 0). 
feature_selection.f_classif(X, y)

h = .02  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

clf = neighbors.KNeighborsClassifier(11, weights='uniform')
clf.fit(X[:, 2:4], y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:, 2].min() - 1, X[:, 2].max() + 1
y_min, y_max = X[:, 3].min() - 1, X[:, 3].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), #h is the step we set
                     np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Plot also the training points
plt.scatter(X[:, 2], X[:, 3], c=y, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("3-Class classification (k = %i, weights = '%s')"
         % (21, 'uniform'))

plt.show()






























