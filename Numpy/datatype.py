'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: Changing datatype 

    '''

import numpy as np
  
# Create a numpy array
arr = np.array([10, 20, 30, 40, 50])
print(arr)
print(arr.dtype)
arr = arr.astype('float64')
print(arr)
print(arr.dtype)