'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: new array
'''

import numpy as np
x= np.arange(12).reshape(3, 4)
print("Original array elements:")
print(x)
for a in np.nditer(x, op_flags=['readwrite']):
    a[...] = 3 * a
print("New array elements:")
print(x)