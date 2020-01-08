# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:54:24 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]



#data_frame=pd.read_csv(input_file,error_bad_lines=False)
#print(data_frame.columns)
#data_frame.rename(columns={'Supplier Name':'Supplier_Name','Invoice Number':'Invoice_Number'},inplace=True)
#print(data_frame.columns)
#data_frame_cols=['supplier name','invoice number','part number','cost','purchase date']
#data_frame.columns=data_frame_cols
#print(data_frame.columns)


#data_frame_cols=['supplier name','invoice number','part number','cost','purchase date']
#data_frame=pd.read_csv(input_file,names=data_frame_cols,header=0,error_bad_lines=False)
#print(data_frame.columns)
#print(data_frame)

data_frame=pd.read_csv(input_file,error_bad_lines=False)
data_frame.columns=data_frame.columns.str.replace(' ','_')
print(data_frame.columns)
print(data_frame)
