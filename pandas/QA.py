# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:41:56 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

#only read two columns
print(pd.read_csv(input_file,usecols=['Supplier Name','Cost']))

#read faster
#read only three rows before reading the entire form
print(pd.read_csv(input_file,nrows=3))

#iteration
for index,row in data_frame.iterrows():
    print(index,row['Supplier Name'],row['Cost'])


#drop non-numeric columns
import numpy as np
print(data_frame.select_dtypes(include=[np.number]))