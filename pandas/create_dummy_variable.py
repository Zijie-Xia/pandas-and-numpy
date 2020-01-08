# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:51:10 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

data_frame['Supplier_X']=data_frame['Supplier Name'].map({'Supplier X':0,'Supplier Y':1,'Supplier Z':2})
print(data_frame)

print(pd.get_dummies(data_frame['Supplier Name']))
print(pd.get_dummies(data_frame['Supplier Name']).iloc[:,1:])
print(pd.get_dummies(data_frame['Supplier Name'],prefix='Supplier'))

Supplier_dummies=pd.get_dummies(data_frame['Supplier Name'],prefix='Supplier')
data_frame=pd.concat([data_frame,Supplier_dummies],axis=1)
print(data_frame)

#how to pass a dataframe to pd.get_dummies
data_frame=pd.read_csv(input_file,error_bad_lines=False)
print(pd.get_dummies(data_frame,columns=['Supplier Name','Purchase Date']))
print(pd.get_dummies(data_frame,columns=['Supplier Name','Purchase Date'],drop_first=True))