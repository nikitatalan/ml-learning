import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)
# number of dimensions
print(a.ndim)
# number of elements along each dimension
print(a.shape)
# total number of elements
print(a.size)

# array of zeros, ones and random elements
zero_arr = np.zeros(4)
ones_arr = np.ones(5)
empty_arr = np.empty(2)

print(zero_arr)
print(ones_arr)
print(empty_arr)

# range of elements: (start, stop, step)
a = np.arange(2, 9, 2)
print(a)
# range of elements: (start, stop, number of elements)
a = np.linspace(0, 10, num = 5)
print(a)

# concatenating arrays
a = np.zeros(3)
b = np.ones(2, dtype = np.float64)
c = np.concatenate((a, b))
print(a, b, c)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
z = np.concatenate((x, y), axis = 0)
print(z)

# reshaping arrays
a = np.arange(6)
b = a.reshape(3, 2)
print(a)
print(b)

# adding a new axis to an array
a1 = np.array([1, 2, 3, 4, 5, 6])
print(a1, a1.shape)
a2 = a1[np.newaxis, :]
print(a2, a2.shape)
a3 = a1[:, np.newaxis]
print(a3, a3.shape)

b1 = np.expand_dims(a1, axis = 0)
b2 = np.expand_dims(a1, axis = 1)
print(b1.shape, b2.shape)

# select values based on conditions
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a > 4])
divisible_by_2 = (a%2 == 0)
print(a[divisible_by_2])

# stacking
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])
# vertical stack
print(np.vstack((a1, a2)))
# horizontal stack
print(np.hstack((a1, a2)))

# sum for different axis
b = np.array([[1, 1],
              [2, 2]])
print(b.sum(axis = 0))
print(b.sum(axis = 1))

# broadcasting
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10).reshape(3, 3)
c = a*b
print(c)

# useful operations
print(c.max())
print(c.min())
print(c.sum())
print(c.mean())
print(c.prod(axis = 1))
print(c.std())

a = np.ones((4, 3, 2))
rng = np.random.default_rng()  # the simplest way to generate random numbers
b = rng.random((3, 2))
print(a)
print(b)
