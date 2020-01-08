# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:16:42 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)
data_frame.drop('Cost',axis=1,inplace=True)
print(data_frame)
data_frame.drop(['Purchase Date','Invoice Number'],axis=1,inplace=True) #axis=1 means columns,not rows;
print(data_frame)
print(data_frame.shape)
data_frame.drop([0,1],axis=0,inplace=True)
print(data_frame)
print(data_frame.shape)