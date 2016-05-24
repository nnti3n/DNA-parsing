from sklearn.externals import joblib
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from scipy.io.arff import loadarff

import scipy as sp
import numpy as np

# load the iris datasets
dataset = loadarff(open('data/vector_output/hbv_80_7class_long.arff', 'r'))
target = np.array(dataset[0]['class'])
data, meta = loadarff(open('data/vector_output/hbv_80_7class_long.arff', 'r'))
train = np.array(data)

# filter
# X = np.asarray(train.tolist(), dtype=np.float32)
train_data = data[meta.names()[:-1]] #everything but the last column
X = train_data.view(np.float).reshape(data.shape + (-1,)) #converts the record array to a normal numpy array

# cross validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
	X, target, test_size=0.1, random_state=0)

# fit a CART model to the data
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

print(rf)
# make predictions
expected = target
predicted = cross_validation.cross_val_predict(rf,X, target, cv=10)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))