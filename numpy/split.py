# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:43:55 2019

@author: 74787
"""

import numpy as np


A=np.arange(12).reshape((3,4))
print(np.split(A,2,axis=1))
print(np.array_split(A,3,axis=1))
print(np.vsplit(A,3))
print(np.hsplit(A,2))