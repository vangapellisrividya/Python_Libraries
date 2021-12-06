'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: length of bytes

    '''

import numpy as np
x = np.array([1,2,3], dtype=np.float64)
print("Size of the array: ", x.size)
print("Length of one array element in bytes: ", x.itemsize)
print("Total bytes consumed by the elements of the array: ", x.nbytes)
