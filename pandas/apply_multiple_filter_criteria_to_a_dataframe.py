# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:16:06 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame[(data_frame['Supplier Name']=='Supplier X') & (data_frame['Part Number']>=5000)])

print(data_frame[(data_frame['Supplier Name']=='Supplier X') | (data_frame['Part Number']>=5000)])

print(data_frame[data_frame['Supplier Name'].isin(['Supplier X','Supplier Y'])])