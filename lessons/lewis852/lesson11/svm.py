import numpy as np
import matplotlib.pyplot as plt


# download SVM, datasets and metrics from sci kit learn
from sklearn import svm, datasets, metrics
iris = datasets.load_iris()

classifier = svm.SVC().fit(iris.data, iris.target)
classifier.predict(iris.data)

print metrics.classification_report(classifier.predict(iris.data), iris.target)

# get support vectors. These are the flowers that contributed to creating our boundary lines. 
# the more support vectors the more likely we are to be over fitted. 
classifier.support_vectors_

# get indices of support vectors
classifier.support_

# get number of support vectors for each class
classifier.n_support_

len(classifier.support_)

# 0.3 very high % of data used as support vectors. 
len(classifier.support_) / 150.0

# To make plotting easier, let's just use the last two features.
# this means from the 2nd column (= 3rd column) until the last. 
X = iris.data[:, 2:]
Y = iris.target
h = .02  # step size in the mesh


# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
# linear SVC is better for large datasets. No kernal parameter. 

C = 1.0  # SVM regularization parameter, our COST value. 

svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, Y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)
lin_svc = svm.LinearSVC(C=C).fit(X, Y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))


# title for the plots
titles = ['SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel',
          'LinearSVC (linear kernel)']


for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].

    plt.subplot(2, 2, i + 1)

    #Z is for all our mesh points make a prediction. 
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis('off')
    
    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
    
    plt.title(titles[i])

plt.show()

























