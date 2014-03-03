from sklearn import datasets, metrics, tree, cross_validation
from matplotlib import pyplot as plt
iris = datasets.load_iris()

y_pred = tree.DecisionTreeClassifier().fit(iris.data, iris.target).predict(iris.data)

print "Number of mislabeled points : %d" % (iris.target != y_pred).sum()
print "Absolutely ridiculously overfit score: %d" % (tree.DecisionTreeClassifier().fit(iris.data, iris.target).score(iris.data, iris.target))

clf = tree.DecisionTreeClassifier()
clf.fit(iris.data, iris.target)

clf.predict(iris.data)

# Confusion Matrices
metrics.confusion_matrix(iris.target, clf.predict(iris.data))

# Precision and Recall
print metrics.classification_report(iris.target, clf.predict(iris.data))

# Generalizing our tree

x_train, x_test, y_train, y_test = cross_validation.train_test_split(iris.data,
    iris.target, test_size=.3)
clf.fit(x_train, y_train)

# Confusion matrix test again
# We can see the split of training and test data in the PRINT output, not optimal
metrics.confusion_matrix(y_train, clf.predict(x_train))
print metrics.classification_report(y_train, clf.predict(x_train))


# Precision and recall
# We can see recall and precision are not 100% for flower 2 because No.2 was mislabelled as a No1.
metrics.confusion_matrix(y_test, clf.predict(x_test))
print metrics.classification_report(y_test, clf.predict(x_test))

# Min samples 
clf.set_params(min_samples_leaf=5)

# Max depth
clf.set_params(max_depth=5)

clf.fit(x_train, y_train)
metrics.confusion_matrix(y_train, clf.predict(x_train))
metrics.confusion_matrix(y_test, clf.predict(x_test))







