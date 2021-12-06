'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: suppression

    '''


# Importing Numpy library 
import numpy as np
  
num = np.array([[3.1415, 2.7182],[6.6260e-34, 6.6743e-11]]) 
print("Numpy array values with precision 3:\n")
np.set_printoptions(precision = 3, suppress = True)
print(num)