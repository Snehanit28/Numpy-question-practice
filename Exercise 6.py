#  How to replace items that satisfy a condition without affecting the original array?

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

new_arr = arr.copy()

# Replace values greater than 3 with 99
new_arr[new_arr > 3] = 99

print(arr)
print(new_arr)
