# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:24:28 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.mean())
print(data_frame.mean(axis=0))
print(data_frame.mean(axis='index'))

print(data_frame.mean(axis=1))
print(data_frame.mean(axis='columns'))