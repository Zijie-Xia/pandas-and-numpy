# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:39:50 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)
data_frame=pd.get_dummies(data_frame,columns=['Supplier Name','Purchase Date'])
print(data_frame)

print(pd.get_option('display.max_rows'))#show how many rows will display at most
pd.set_option('display.max_rows',None)#show all rows
pd.reset_option('display.max_rows')

print(pd.get_option('display.max_columns'))
pd.set_option('display.max_columns',20)
print(data_frame)

#if some info is hidden as '...' but I want to display it
print(pd.get_option('display.max_colwidth'))
pd.set_option('display.max_colwidth',1000)#None is no admitted,but you can set a large number

#change the number of decimal points
data_frame['Part Number']=data_frame['Part Number'].astype(float)
pd.get_option('display.precision',1)
print(data_frame)

#use comma in float or int
pd.set_option('display.float_format','{:,}'.format)
print(data_frame)

print(pd.describe_option())
print(pd.describe_option('columns'))

#change all the options to the default
pd.reset_option('all')