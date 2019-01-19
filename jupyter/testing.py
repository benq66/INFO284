import numpy as np
from scipy import sparse
from IPython.display import display
import matplotlib.pyplot as plt
import mglearn

# A NumPy array looks like this:
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('x:\n{}' .format(x))

# Sparse matrices are used whenever we want to store a 2D array that contains mostly zeros.
# Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else:
eye = np.eye(5)
print('NumPy array:\n{}' .format(eye))

# Convert the NumPy array to a SciPy sparse matrix in CSR format (CRS - compressed row storage)
# Only the nonzero entries are stored
sparse_matrix = sparse.csr_matrix(eye)
print('\nSciPy sparse CSR matrix:\n{}' .format(sparse_matrix))

# A way to create the same sparse matrix as before, using the COO (Coordinate list) format:
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n{}" .format(eye_coo))

# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
# Create a second array using sine
y = np.sin(x)
# The plot function makes a line chart of one array against another
# plt.plot(x, y, marker='x')
plt.show(plt.plot(x, y, marker='x'))

# A small example of creating a DataFrame using a dictionary:
import pandas as pd

# create a simple dataset of people
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Location': ['New York', 'Paris', 'Berlin', 'London'],
        'Age': [24, 13, 53, 33]
        }

data_pandas = pd.DataFrame(data)
display(data_pandas)
