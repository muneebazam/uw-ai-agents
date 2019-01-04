import numpy as np
import pandas as pd
import graphviz as gv
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

# EDIT THIS LINE WITH THE MAXIMUM DEPTH REQUIRED
maximum_depth=10

for i in range(1,maximum_depth+1):

	data = pd.read_csv('data_set.csv', sep= ',', header= None)

	X = data.values[:, 0:4]
	Y = data.values[:,4]

	kf = KFold(n_splits=10)
	kf.get_n_splits(X);
	iter_num = 0

	print "Testing for depth: ", i

	training = 0
	test = 0

	for train_index, test_index in kf.split(X):

		X_train, X_test = X[train_index], X[test_index]
		y_train, y_test = Y[train_index], Y[test_index]
	 	
		clf_entropy = DecisionTreeClassifier(criterion = "entropy", max_depth=i, random_state = 100)
		clf_entropy.fit(X_train, y_train)

		y_pred = clf_entropy.predict(X_test)
		y_pred2 = clf_entropy.predict(X_train)

		training += accuracy_score(y_train,y_pred2)*100
		test += accuracy_score(y_test,y_pred)*100

		dot_data = tree.export_graphviz(
			clf_entropy,
			out_file=None,
			feature_names=['sepal length', 'sepal width', 'petal length', 'petal width'],
			class_names=['setosa', 'versicolor', 'virginica'],
			filled=True,
			rounded=True,
			special_characters=True
			)

		graph = gv.Source(dot_data)
		graph.render(filename="depth-" + str(i) + '-iter-' + str(iter_num))
		iter_num += 1

	training_avg = training / 10
	test_avg = test / 10

	print "The average training set accuracy is: ", training_avg
	print "The average validation set accuracy is: ", test_avg
	print ""

