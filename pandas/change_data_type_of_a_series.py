# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:37:41 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.Cost.str.replace('$','').astype(float))

#the average of total cost
print(data_frame.Cost.str.replace('$','').astype(float).mean())

#look for Supplier X and output 0 or 1 
print(data_frame['Supplier Name'].str.contains('X').astype(int))

#define type of each column before reading csv
#print(pd.read_csv(input_file,dtype={'Part Number':float}))