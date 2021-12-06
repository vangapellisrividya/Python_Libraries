'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: add column in array

    '''

import numpy as np
x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])
print(np.append(x, y, axis=1))
