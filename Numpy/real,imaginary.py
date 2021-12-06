'''
    Created on Dec 5, 2021

    @author:srividya
    @Date:  5/12/2021
    @Title: real and imaginary values

    '''

import numpy as np
  
# creating a NumPy array
complex_num = np.array([-1 + 9j, 2 - 77j,31 - 25j, 40 - 311j,72 + 11j])
for i in range(len(complex_num)):
      print("{}. complex number is {}".format(i + 1, complex_num[i]))
      print ("The real part is: {}".format(complex_num[i].real))
      print ("The imaginary part is: {}\n".format(complex_num[i].imag))