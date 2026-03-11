# Importing Libraries
import numpy as np


array_1 = np.array([[1, 2, 3, 4]])
array_2 = np.array([[1], [2], [3], [4]])

# Printing the shapes of the arrays
print("Shape of array_1:", array_1.shape)
print("Shape of array_2:", array_2.shape)


# Making a multiplication of 1 to 10 using broadcasting
# array_1 = np.arange(1, 11) # similar to np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# array_2 = np.arange(1, 11).reshape(10, 1) # similar to np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

# Printing the multiplication of array_1 and array_2
print(array_1 * array_2)