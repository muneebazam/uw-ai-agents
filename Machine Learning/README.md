Decision Tree Learning
======================

Implementation of a decision tree learning algorithm with the help of the scikit-learn Python machine learning library. 

The algorithm takes as input a ```<max_depth>``` parameter and builds decision trees with depth starting at 1 up to the maximum specified. 

This algorithm uses ten-fold cross validation to build and train on the same dataset. This means the data set is split into ten equal sections with ten rounds of learning in which 1/10th of the data set is used as a validation test and the rest is used for training. This way we get to train and validate on all the data in turns to maximize prediction accuracy. 

For more information on cross validation see: *https://machinelearningmastery.com/k-fold-cross-validation/*

### Data Set

The learning algorithm will classify samples of the Iris flower into one of three categories depending on its features.

The *data_set.csv* file contains 100 data points each with four features and a classification. The features are *sepal length (cm)*, *sepal width (cm)*, *petal length (cm)* and *petal width (cm)*. The classifications are *Iris setosa*, *Iris veriscolor* and *Iris virginica*.

### Usage

```python decision_trees.py <max_depth>``` Where ```<max_depth>``` is the maximum tree depth the algorithm will build.

***Note: this algorithm will export a file with a visual of the decision tree it creates for every depth/iteration. For example, running the algorithm with max_depth=10 will generate 100 files (10 iterations with depth=1, 10 iterations with depth=2 and so on)***


