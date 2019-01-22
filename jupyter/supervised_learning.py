import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import numpy as np

"""
Chapter 2. Supervised Learning.
Classification and regression examples, plus several other algorithms.
"""

# an example of a synthetic two-class classification dataset
# a scatter plot visualizing all of the data points in this dataset

# # generate dataset
# X, y = mglearn.datasets.make_forge()
# # plot dataset
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# plt.legend(['Class 0', 'Class 1'], loc=4)
# plt.xlabel('First feature')
# plt.ylabel('Second feature')
# print("X.shape: {}" .format(X.shape))
# plt.show()

# X, y = mglearn.datasets.make_wave(n_samples=40)
# plt.plot(X, y, 'o')
# plt.ylim(-3, 3)
# plt.xlabel("Feature")
# plt.ylabel("Target")
# plt.show()

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("cancer.keys(): \n{}" .format(cancer.keys()))
print("Shape of cancer data: {}" .format(cancer.data.shape))
print("Sample counts per class:\n{}" .format(
      {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))
print("Feature names:\n{}" .format(cancer.feature_names))

from sklearn.datasets import load_boston
boston = load_boston()
print("boston.data shape: {}" .format(boston.data.shape))
X, y = mglearn.datasets.load_extended_boston()
print("X.shape: {}" .format(X.shape))
# mglearn.plots.plot_knn_classification(n_neighbors=1)
# mglearn.plots.plot_knn_classification(n_neighbors=3)
# plt.show()

from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
print("Test set predictions: {}" .format(clf.predict(X_test)))
print("Test set accuracy: {:.2f}" .format(clf.score(X_test, y_test)))

fig, axes = plt.subplots(1, 3, figsize=(10, 3))

for n_neighbors, ax in zip([1, 3, 9], axes):
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{} neighbor(s)" .format(n_neighbors))
    ax.set_xlabel("feature 0")
    ax.set_ylabel("feature 1")
axes[0].legend(loc=3)
plt.show()
