# lab2

# from sklearn.linear_model import LinearRegression
#
# # print(help(5))
# list_orig = [1, 2, 3]
# list_copy = list_orig[:]
#
# for x in range(0, 10):
#     print(x)
# else:
#     print('Ends with {}'.format(x))
#
# my_dict = {1: 1, 2: 2, 3: 3}
# for key, value in my_dict.items():
#     print('Key: {} Value: {}'.format(key, value))
#
#
# # class
# class MyClass:
#     y = 0
#
#     def __init__(self, y=10):
#         self.y = y
#
#     def func(self):
#         print(self.y)
#
#
# file1 = open('stien til en mappe', 'w')
# file1.write('1')
#
# try:
#     print(1)
# except ValueError:
#     print('invalid input')
# else:
#     print(1)
# finally:
#     print(2)

import numpy as np

b = np.array([1, 2, 3], ndmin=2)
print(b)

b = np.zeros((4, 5))
print(b)

b = np.ones((4, 5))
print(b)

b = np.empty((2, 3))
print(b)

b = np.random.random((2, 3))*10
print(b)

b = np.arange(4, 10)
print(b)

b = np.arange(4, 10, 2)
print(b)

b = np.arange(0, 3, 0.5)
print(b)

b = np.linspace(0, 3, 100)
print(b)

b = np.arange(20).reshape(4, 5)
print(b)

print('b shape: {}' .format(b.shape))
# b.ndim
# b.dtype

# matrix product
# A @ B

for element in b.flat:
    print(element, sep=' ', end=' ')

print()
print(b.ravel())

print(b.reshape(5, 4))

import matplotlib.pyplot as plt

# y = np.arange(6)
# plt.plot(y)
# plt.ylabel("Numbers")
# plt.xlabel("Autofilled sequence")
# plt.show()

z = np.random.random(20)*10
ticks = np.arange(0, 10, 0.5)
plt.yticks(ticks)

plt.annotate('Look at this spot', xy=(4, z[4]))
plt.plot(z)
plt.show()

# plt.plot(z, linestyle=':')

# 'bs'- square, 'g^' - triangle

# subplots

# fig, ((bar_plot, pie_chart), (scatter_plot, image_plot)) = plt.subplots(2, 2, sharex=False, sharey=False)
# img = mpimg.imgread('dog.png')

# pandas.date_range