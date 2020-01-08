# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:22:04 2019

@author: 74787
"""

import numpy as np

A=np.array([1,1,1])
B=np.array([2,2,2])
print(np.vstack((A,B)))#vertical stack
print(np.hstack((A,B)))#horizontal stack
print(np.concatenate((A,B),axis=0))
A=A.reshape(3,1)
B=B.reshape(3,1)
print(np.concatenate((A,B),axis=1))