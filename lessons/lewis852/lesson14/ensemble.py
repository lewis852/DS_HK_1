from sklearn.cross_validation import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier

X, y = make_blobs(n_samples=10000, n_features=10, centers=100,
     random_state=0)

## DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=None, min_samples_split=1,
       random_state=0)
scores = cross_val_score(clf, X, y)
scores.mean()

## RandomForestClassifier
# estimators is the number of base classifers 
# min samples = 1 terrible overfitting
# n estimators is the number of Base Classifiers

clf = RandomForestClassifier(n_estimators=10, max_depth=None,
     min_samples_split=1, random_state=0)
scores = cross_val_score(clf, X, y)
scores.mean()

## ExtraTreesClassifier
clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,
    min_samples_split=1, random_state=0)
scores = cross_val_score(clf, X, y)
scores.mean() > 0.999


