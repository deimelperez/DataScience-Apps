import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()

clf.fit(X, Y)

pickle.dump(clf, open('Iris/iris_clf.pkl', 'wb'))
