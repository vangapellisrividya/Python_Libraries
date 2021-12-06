'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: checkerboard patternusing NumPy

    '''

import numpy as np
x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)