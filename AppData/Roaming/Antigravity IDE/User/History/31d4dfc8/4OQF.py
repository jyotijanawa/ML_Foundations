import numpy as np
data = np.random.rand(2,3,4)
zeroes = np.zeros((2,2,2))
full = np.full((2,2,2), (7))
ones = np.ones((2,2,2))
print(data)
print(ones)
print(zeroes)
print(full)


arr = np.array([1,2,3,4],[1,2,3,4])
print(arr)
shape = data.shape
size = data.size
types = data.dtype
print(types)
print(size)
print(shape)

arr = data[0]
slicer = data[0:2]
reverse = data[-1]
singleval = data[0][0][0]
print(arr)
print(slicer)
print(reverse)
print(singleval)
