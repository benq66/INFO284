import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

"""
Chapter 2. Supervised Learning.
Classification and regression examples, plus several other algorithms.
"""

# an example of a synthetic two-class classification dataset
# a scatter plot visualizing all of the data points in this dataset

# generate dataset
X, y = mglearn.datasets.make_forge()
# plot dataset
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(['Class 0', 'Class 1'], loc=4)
plt.xlabel('First feature')
plt.ylabel('Second feature')
print("X.shape: {}" .format(X.shape))
plt.show()
