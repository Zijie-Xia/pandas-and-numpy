# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:37:17 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.drop('Purchase Date',axis=1))
print(data_frame)
data_frame.drop('Purchase Date',axis=1,inplace=True)
print(data_frame)

print(data_frame.dropna(how='any'))
data_frame.dropna(how='any',inplace=True)
print(data_frame)

#other:sort_values,set_index
data_frame.set_index('Supplier Name',inplace=True)
print(data_frame)
#data_frame=data_frame.set_index('Supplier Name')
#print(data_frame)