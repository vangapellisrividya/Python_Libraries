'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: Onedimensional array using NumPy

    '''


import numpy as np
ini_array = np.array([1, 2, 3, 6, 4, 5])
print("initial array", str(ini_array))
print("type of ini_array", type(ini_array))
res = np.flipud(ini_array)
print("final array", str(res))