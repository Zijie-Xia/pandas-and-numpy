# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:20:11 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.index)
print(data_frame.columns)
print(data_frame.shape)

#for identification
print(data_frame[data_frame['Supplier Name']=='Supplier X'])

#for selection
print(data_frame.loc[5,'Cost'])

#change index
#why use index
data_frame.set_index('Cost',inplace=True)
print(data_frame)
print(data_frame.index)
print(data_frame.columns)
print(data_frame.shape)
#if want to delete the name of index
data_frame.index.name=None
print(data_frame)

#move index back to columns
data_frame.index.name='Cost'
data_frame.reset_index(inplace=True)
print(data_frame)

#why use index
print(data_frame['Part Number'].describe().loc['mean'])

data_frame.set_index('Cost',inplace=True)
print(data_frame['Supplier Name'])
print(data_frame['Supplier Name'].value_counts())
print(data_frame['Supplier Name'].value_counts().index)
print(data_frame['Supplier Name'].value_counts().values)
print(data_frame['Supplier Name'].value_counts()['Supplier X'])
print(data_frame['Supplier Name'].value_counts().sort_index())
print(data_frame['Supplier Name'].value_counts().sort_values())

#multiple two columns
number2=pd.Series([3000000,85000],index=['Supplier X','Supplier Y'],name='Total Number')
print(number2)
data_frame.index.name='Cost'
data_frame.reset_index(inplace=True)
data_frame.set_index('Supplier Name',inplace=True)
print(data_frame)
print(data_frame.Cost.str.replace('$','').astype(float)*number2)
#add one column to a data frame
data_frame.reset_index(inplace=True)
number3=pd.Series([3000000,85000],name='Total Number')
print(pd.concat([data_frame,number3],axis=1))
#useless,why?
#data_frame.set_index('Purchase Date',inplace=True)
#number4=pd.Series([3000000,85000,67694],index=['2/10/14','2/17/14','2/24/14'],name='Total Number')
#print(pd.concat([data_frame,number4]))