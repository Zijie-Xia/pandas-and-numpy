# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:34:49 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.Cost.sort_values())#print just one column of the dataframe
print(data_frame.Cost.sort_values(ascending=False))

print(data_frame.sort_values('Cost'))#print the entire dataframe
print(data_frame.sort_values('Cost',ascending=False))

#.sort() and .order() are useless here

#by multiple columns
print(data_frame.sort_values(['Cost','Purchase Date']))
print(data_frame.sort_values(['Cost','Purchase Date'],ascending=False))