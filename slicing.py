# importing libraries
import numpy as np


# creating a 2-D array
array = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

# To slice an array, you need the start, end, step
print(array[:2, :2])

# print(array.shape)
# print(array.ndim)