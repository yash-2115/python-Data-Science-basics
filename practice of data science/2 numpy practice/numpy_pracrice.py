import numpy as np

one_dimention = np.array([1, 2, "Yash Patel", 3+1j])
two_dimention = np.array([[1,2], [3,4], [5,6]])

print(one_dimention)
print(two_dimention)

# ndim funtion
print(one_dimention.ndim)
print(two_dimention.ndim)

# itrmsize funtion
print(one_dimention.itemsize)
print(two_dimention.itemsize)

# size function
print(one_dimention.size)
print(two_dimention.size)

# zeros and once function
print(np.zeros((3,2)))
print('')
print(np.ones((2,3)))

# arange function
print(np.arange(1,100))
print(np.arange(1,100,10))

# linespace function
print(np.linspace(1,100,10))

# reshape function
print(two_dimention.reshape(3,2))

# revel function
print(two_dimention.ravel())

# min fucntion
print(two_dimention.min())

# max funtion
print(two_dimention.max())

# sum function
print(two_dimention.sum())

# sum sqrt
print(np.sqrt(two_dimention))

# std function
print(np.std(two_dimention))

# some operations
a = np.array([[1,2], [3,4]])
b = np.array([[1,2], [3,4]])

print(a * b)
print(a / b)
print(a + b)
print(a.dot(b))