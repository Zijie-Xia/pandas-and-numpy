# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:46:22 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

#NaN means missing
print(data_frame.isnull())

print(data_frame.notnull())

print(data_frame.notnull().sum())

print(data_frame.notnull().sum(axis=0))

print(data_frame.notnull().sum(axis=1))

#how to deal with the missing values
#find
print(data_frame.dropna(how='any'))#drop a row if any of its values are missing
print(data_frame.dropna(how='all'))#only drop a row if all of its values are missing
print(data_frame.dropna(subset=['Supplier Name','Cost'],how='any'))#drop a row if either of the values of the two columns is missing
print(data_frame.Cost.value_counts(dropna=False))#include the number of NaN

#fill
data_frame.Cost.fillna(value='$0.00',inplace=True)
print(data_frame)