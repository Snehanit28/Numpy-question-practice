#  How to extract items that satisfy a given condition from 1D array?

import numpy as np

arr = np.array([5, 12, 7, 20, 3, 15])
result = arr[arr > 10]

print(result)   # => [12 20 15]