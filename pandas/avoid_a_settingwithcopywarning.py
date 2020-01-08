# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 00:00:47 2019

@author: 74787
"""

import sys 
import pandas as pd
import numpy as np
input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

#solution:use .loc to specify each row and each colunm
data_frame.loc[data_frame['Supplier Name']=='Supplier Z','Supplier Name']=np.nan
print(data_frame)

#solution:use .copy() to make sure it is a copy,not a view
new_data_frame=data_frame.loc[data_frame['Part Number']<=6000,:].copy()
new_data_frame.loc[0,'Part Number']=6000
print(new_data_frame)