# Importing libraries
import numpy as np


# randoms numbers using default_rng()
rng = np.random.default_rng()

# print(rng.integers(1, 7))
# print(rng.integers(low=1, high=7))
# print(rng.integers(low=1, high=101, size=(3, 5)))

# Random floating numbers using uniform(). The uniform function makes every number range possible or have a probability of been selected

# print(np.random.uniform(0, 1))

# setting the seed
# np.random.seed(42)

# print(np.random.uniform(low=-1, high=1, size=(3, 5)))

# Shuffling an array

# rng = np.random.default_rng()

# # 1-D array
# array = np.array([1, 2, 3, 4, 5])
# rng.shuffle(array)
# print(array)


# Making Random Choice
rng = np.random.default_rng()

# 1-D array of Fruits
fruits = np.array(["🍏", "🥭", "🍍", "🥥", "🍊"])
fruit = rng.choice(fruits, size=(3, 3))
# print(fruits)
print(fruit)




