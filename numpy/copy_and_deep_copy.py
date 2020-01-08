# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:50:53 2019

@author: 74787
"""

import numpy as np
import copy

a=np.arange(4)
#copy
b=a
c=a
d=b
a[0]=10
print(a,b,c,d)
d[1:3]=[20,30]
print(a,b,c,d)

#deep copy
b=copy.deepcopy(a)
a[3]=40
print(a,b,c,d)