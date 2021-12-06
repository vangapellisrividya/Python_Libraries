'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: immutable array

    '''
import numpy as np
x = np.zeros(10)
x.flags.writeable = False
print("Test the array is read-only or not:")
print("Try to change the value of the first element:")
x[0] = 1
