# Importing libraries
import numpy as np


# Filtering: selecting elements from an array based on a condition

# 2-D array
ages = np.array([[22, 83, 17, 56, 11, 49, 1, 35],
                 [93, 17, 76, 55, 21, 88, 60, 10]])


# ages less than 18 using boolean filtering
teenagers = ages[ages < 18]
adults = ages[ages >= 18]
seniors = ages[ages >= 65]

adults = ages[(ages >= 18) & (ages <= 65)]


# Using the where parameter
adults = np.where(ages > 18, ages, 0)

# print(teenagers)
# print(adults)
# print(seniors)
print(adults)