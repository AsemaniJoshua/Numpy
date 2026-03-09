# Importing libraries
import numpy as np


# definning a numpy array
zero_dimension = np.array('A')
first_dimension = np.array(['A','B','C'])
second_dimension = np.array([
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
    ])


third_dimension = np.array([
    [['A','B','C'], ['D','E','F'], ['G','H','I']],
    [['J','K','L'], ['M','N','O'], ['P','Q','R']],
    [['S','T','U'], ['V','U','X'], ['Y','Z','']]
    ])


# chain indexing
letter = third_dimension[0][0][0]

# Multidimensional indexing
letter = third_dimension[0,0,0]


# forming a word base on multi-dimensional indexing
word = third_dimension[0,0,0] + third_dimension[1,1,1] + third_dimension[2,0,1]

# checking the shape and dimensions
# print(zero_dimension.shape)
# print(zero_dimension.ndim)

# print(first_dimension.shape)
# print(first_dimension.ndim)

# print(second_dimension.shape)
# print(second_dimension.ndim)

# print(third_dimension.shape)
# print(third_dimension.ndim)

# print(letter)

print(word)