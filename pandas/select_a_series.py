# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:11:17 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)
print(type(data_frame))
print(data_frame['Cost'])
print(data_frame['Purchase Date'])
print(data_frame.Cost)
data_frame['Something']=data_frame.Cost+data_frame['Purchase Date']
print(data_frame)
