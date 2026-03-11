# importing libraries
import numpy as np


# Aggregate functions: combines all the elements in an array and returns a single value


# A 2-D array
array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


# sum, mean, median, min, max, std, var
# print("Sum:", np.sum(array_2d))
# print("Mean:", np.mean(array_2d))
# print("Median:", np.median(array_2d))
# print("Min:", np.min(array_2d))
# print("Max:", np.max(array_2d))
# print("Std:", np.std(array_2d))
# print("Var:", np.var(array_2d))


# index of the minimum and maximum values
# print("Index of minimum value:", np.argmin(array_2d))
# print("Index of maximum value:", np.argmax(array_2d))



# summing array based on columns
print("Sum based on columns:", np.sum(array_2d, axis=0))



# summing array based on rows
print("Sum based on rows:", np.sum(array_2d, axis=1))
