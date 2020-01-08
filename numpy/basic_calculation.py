# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:36:40 2019

@author: 74787
"""

import numpy as np

a=np.arange(0,17,2).reshape((3,3))
b=np.ones((3,3))
print(a-b)
print(a**2-b)
print(np.cos(a))
print(a<3)
print(a*b)
c1=np.dot(a,b)
print(c1)
c2=a.dot(b)
print(c2)

d=np.random.random((2,4))
print(d)
print(np.sum(d))
print(np.sum(d,axis=1))
print(np.max(d))
print(np.min(d))
print(np.argmax(d))
print(np.mean(d))
print(d.mean())
print(np.average(d))
print(np.median(d))
print(np.cumsum(d))#accumulation sum
print(np.diff(d))
print(np.nonzero(d))#output the position of the nonzero value
print(np.sort(d))
print(np.transpose(d))
print(d.T)
print(d.T.dot(d))
print(np.clip(d,0.2,0.8))#if the value is less than 0.2,the output is 0.2;if the value is more than 0.8,the output is 0.8;other value does not change
