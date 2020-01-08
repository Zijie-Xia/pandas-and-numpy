# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:42:46 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

#map is a series method
data_frame['Supplier Name Number']=data_frame['Supplier Name'].map({'Supplier X':0,'Supplier Y':1,'Supplier Z':2})
print(data_frame.loc[:,['Supplier Name','Supplier Name Number']])

#apply is both a seires and dataframe method
#use apply as a series method
data_frame['Supplier Name Length']=data_frame['Supplier Name'].apply(len)
print(data_frame.loc[:,['Supplier Name','Supplier Name Length']])
#it is wrong
data_frame['Supplier Name Length2']=len(data_frame['Supplier Name'].str.strip())
print(data_frame.loc[:,['Supplier Name','Supplier Name Length2']])

import numpy as np
data_frame['Part Number Ceil']=data_frame['Part Number'].apply(np.ceil)
print(data_frame.loc[:,['Part Number','Part Number Ceil']])

def get_element(my_list,position):
    return my_list[position]
print(data_frame['Supplier Name'].str.split(' ').apply(get_element,position=1))

print(data_frame['Supplier Name'].str.split(' ').apply(lambda x:x[1]))

#use apply as a dataframe method
print(data_frame.loc[:,['Supplier Name Length','Part Number','Part Number Ceil']].apply(max,axis=0))
print(data_frame.loc[:,['Supplier Name Length','Part Number','Part Number Ceil']].apply(max,axis=1))
print(data_frame.loc[:,['Supplier Name Length','Part Number','Part Number Ceil']].apply(np.argmax,axis=0))
print(data_frame.loc[:,['Supplier Name Length','Part Number','Part Number Ceil']].apply(np.argmax,axis=1))

#applymap is to apply a function to every element of a dataframe

print(data_frame.loc[:,['Supplier Name Length','Part Number','Part Number Ceil']].applymap(float))