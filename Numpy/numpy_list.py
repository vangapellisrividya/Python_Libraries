'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: converting numpy to list

    '''

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f'NumPy Array:\n{arr}')
list1 = arr.tolist()
print(f'List: {list1}')