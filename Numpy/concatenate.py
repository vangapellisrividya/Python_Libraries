'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: concatenate numpy array

    '''

import numpy as np
 
# Creating two 2D arrays
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(10,19).reshape(3,3)
print(arr1)
print(arr2)
print(np.concatenate((arr1,arr2),axis=1))