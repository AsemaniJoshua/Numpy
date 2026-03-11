# Importing libraries
import numpy as np


# creating a 1-D array
array_1d = np.array([1.4, 2.2, 3.7, 4.0, 5.])

# Scalar arithmetic

# print(array_1d + 2)
# print(array_1d - 2)
# print(array_1d * 2)
# print(array_1d / 2)
# print(array_1d ** 2)

# Vectorized math func
# print(np.sqrt(array_1d))
# print(np.round(array_1d, 0))
# print(np.floor(array_1d))
# print(np.ceil(array_1d))


# Element-wise arithmetic
array_1 = np.array([1, 2, 3, 4, 5])
array_2 = np.array([5, 4, 3, 2, 1])

# print(array_1 + array_2)
# print(array_1 - array_2)
# print(array_1 * array_2)
# print(array_1 / array_2)
# print(array_1 ** array_2)


# Comparison operators (returns a boolean array)
# print(array_1 > array_2)
# print(array_1 < array_2)
# print(array_1 == array_2)
# print(array_1 != array_2)
array_1[array_1 > 4] = 0
print(array_1)