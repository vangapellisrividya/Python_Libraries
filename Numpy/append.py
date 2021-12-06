'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: appending element of NumPy

    '''

import numpy as np
  

arr = np.array([1, 8, 3, 3, 5])
print('Original Array : ', arr)
arr = np.append(arr, [7])
print('Array after appending : ', arr)