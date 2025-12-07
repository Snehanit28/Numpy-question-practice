#  How to replace items that satisfy a condition with another value in numpy array?

import numpy as np

arr = np.array([5, 12, 7, 20, 3, 15])

arr[arr > 10] = 0   # Replace values > 10 with 0

print(arr)