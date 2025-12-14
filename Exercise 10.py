#  How to generate custom sequences in numpy without hardcoding?

import numpy as np

seq = np.arange(5, 30, 5) 
print(seq)     # => [ 5 10 15 20 25]

a = np.array([1,2,3])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])     # => [1 1 1 2 2 2 3 3 3 1 2 3 1 2 3 1 2 3]
