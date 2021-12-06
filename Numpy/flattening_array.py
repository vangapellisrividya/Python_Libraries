'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: flattening array

    '''

import numpy as np
  
# Creating 2D array
arr = np.array([[5, 6, 7], [8, 9, 10]])
print("Original array:\n", arr)
flattened_array = np.ravel(arr)
print("New flattened array:\n", flattened_array)