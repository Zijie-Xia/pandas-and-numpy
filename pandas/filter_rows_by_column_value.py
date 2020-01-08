# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:14:47 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

#booleans=[]
#for num in data_frame['Part Number']:
#    if num>=5000:
#        booleans.append(True)
#    else:
#        booleans.append(False)
#is_much=pd.Series(booleans)
#print(data_frame[is_much])

#is_much=data_frame['Part Number']>=5000        
#print(data_frame[is_much])

#print(data_frame[data_frame['Part Number']>=5000])
#
#print(data_frame[data_frame['Supplier Name']=='Supplier X'][data_frame['Part Number']>=5000])

print(data_frame.loc[(data_frame['Part Number']>=5000) & (data_frame['Supplier Name']=='Supplier X')])

print(data_frame.loc[data_frame['Supplier Name']=='Supplier X','Part Number'])