# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:12:20 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
user_cols=['Supplier_Name','Invoice_Number','Part_Number','Cost','Purchase_Date']
data_frame=pd.read_csv(input_file,error_bad_lines=False)
print(data_frame)
