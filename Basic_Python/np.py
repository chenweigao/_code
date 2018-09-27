import numpy as np 
from numpy.linalg import *

# list = np.array([[3, 1, -1, 2], [-5, 1, 3, -4], [1, 3, -2, 2], [1, -5, 3, -3]])
list=np.array([[2, 2, -2], [2, -1, 0], [-4, 2, 5]])
print(list)
result = det(list)
print(result)
print("{:.0f}".format(result))
