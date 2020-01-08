# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:19:23 2019

@author: 74787
"""


import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

#loc
print(data_frame.loc[0,:])
print(data_frame.loc[[0,1,2],:])
print(data_frame.loc[0:2,:])

print(data_frame.loc[:,'Cost'])
print(data_frame.loc[:,['Cost','Purchase Date']])
print(data_frame.loc[:,'Invoice Number':'Cost'])
print(data_frame.drop(['Supplier Name','Purchase Date'],axis=1))

print(data_frame[data_frame['Supplier Name']=='Supplier X'])
print(data_frame.loc[data_frame['Supplier Name']=='Supplier X',:])

print(data_frame[data_frame['Supplier Name']=='Supplier X'].Cost)
print(data_frame.loc[data_frame['Supplier Name']=='Supplier X','Cost'])

#iloc:interger position
print(data_frame.iloc[:,[0,3]])
print(data_frame.iloc[:,0:3])#inclusive of 0 and exclusive of 3,list(range(0,3))=[0,1,2]

#ix not reconmend
print(data_frame.ix[7,0])
print(data_frame.ix[0,'Cost'])