# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:23:18 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame['Purchase Date'].str.slice(-5,-3).astype(int))

#to pandas special datetime format
data_frame['Purchase Date']=pd.to_datetime(data_frame['Purchase Date'])
print(data_frame.dtypes)
print(data_frame['Purchase Date'].dt.month)
print(data_frame['Purchase Date'].dt.weekday)
print(data_frame['Purchase Date'].dt.weekday_name)
print(data_frame['Purchase Date'].dt.dayofyear)

ts=pd.to_datetime('5/21/14')
print(data_frame.loc[data_frame['Purchase Date']<=ts,:])
print(data_frame['Purchase Date'].max())
print(data_frame['Purchase Date'].min())
print(data_frame['Purchase Date'].max()-data_frame['Purchase Date'].min())