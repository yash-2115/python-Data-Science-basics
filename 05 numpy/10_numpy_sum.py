import numpy as np

array_2 = np.array([[1,2], [3,4], [5,6]])
# print(array_2.sum())/
print(array_2.sum(axis=0))
print(array_2.sum(axis=1))