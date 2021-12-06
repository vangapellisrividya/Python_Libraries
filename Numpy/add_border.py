'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: Adding border around an existing array

    '''
import numpy as np
array = np.ones((3, 3))
print("Original array")
print(array)
print("\n0 on the border and 1 inside the array")
array = np.pad(array, pad_width=1, mode='constant',constant_values=0)
print(array)
