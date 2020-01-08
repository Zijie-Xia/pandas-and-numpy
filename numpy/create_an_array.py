# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:36:38 2019

@author: 74787
"""

import numpy as np

a=np.array([1,2,3],dtype=np.int)
print(a)
b=np.array([[1,2,3],[4,5,6]])
print(b)
c=np.zeros((3,4))
print(c)
d=np.empty((3,4))
print(d)
e=np.arange(10,20,2)
print(e)
f=np.arange(12)
print(f)
g=np.linspace(0,10,20)
print(g.reshape((4,5)))