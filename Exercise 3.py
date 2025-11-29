#  How to create a boolean array?

import numpy as np

arr = np.array([True, False, True, True])
print(arr)        # => [ True False  True  True]

arr1 = np.array([1,2,3,4,5,6,7,8])
boolean_arr = arr1<5 
print(boolean_arr)    # => [ True  True  True  True False False False False]