# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:13:18 2019

@author: 74787
"""

import numpy as np

A=np.arange(3,15).reshape(3,4)
print(A)
print(A[2])#find the third row
print(A[1,1])
print(A[1,:])
for row in A:
    print(row)
for col in A.T:
    print(col)
print(A.flat)
print(A.flatten())
for item in A.flat:
    print(item)
for item in A.flatten():
    print(item)