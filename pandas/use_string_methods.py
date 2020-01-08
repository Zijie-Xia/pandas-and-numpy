# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:27:34 2019

@author: 74787
"""


import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame['Supplier Name'].str.upper())
print(data_frame['Supplier Name'].str.contains('X'))
print(data_frame[data_frame['Supplier Name'].str.contains('X')])
print(data_frame['Cost'].str.replace('$',''))
print(data_frame['Cost'].str.replace('$','').str.replace('.',''))