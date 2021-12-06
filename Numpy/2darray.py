'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: 2d array using NumPy

    '''

import numpy as np
n=5
border_array = np.ones((n, n), dtype = int)
border_array[1:-1, 1:-1] = 0
print(border_array)