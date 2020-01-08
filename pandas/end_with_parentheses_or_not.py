# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:39:17 2019

@author: 74787
"""

import sys 
import pandas as pd

#input_file=sys.argv[1]
#data_frame=pd.read_csv(input_file,error_bad_lines=False)
data_frame=pd.DataFrame({'A':['a1','a2','a3'],'B':['b1','b2','b3'],'C':['c1','c2','c3']})
data_frame=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'])
print(data_frame.shape)
print(data_frame.dtypes)
print(data_frame.describe())
print(data_frame.describe(include=['object']))  