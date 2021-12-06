'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: common values between ttwo arrays of NumPy

    '''

import numpy as np
ar1 = np.array([0, 1, 2, 3, 4])
ar2 = [1, 3, 4]
print(np.intersect1d(ar1, ar2))