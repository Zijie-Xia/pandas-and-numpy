# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:25:33 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

#whether it is identical with another above
print(data_frame['Supplier Name'].duplicated())
print(data_frame['Supplier Name'].duplicated().sum())

#whether the whole row is identical with a row above
print(data_frame.duplicated())

print(data_frame.loc[data_frame.duplicated(),:])
print(data_frame.loc[data_frame.duplicated(keep='first'),:])
print(data_frame.loc[data_frame.duplicated(keep='last'),:])
print(data_frame.loc[data_frame.duplicated(keep=False),:])
print(data_frame.drop_duplicates(keep='first'))
print(data_frame.drop_duplicates(keep=False))

print(data_frame.duplicated(subset='Supplier Name'))
print(data_frame.duplicated(subset=['Supplier Name','Purchase Date']))
print(data_frame.drop_duplicates(subset=['Supplier Name','Purchase Date']))