# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:56:55 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.sample(n=3))
print(data_frame.sample(n=3,random_state=3))
print(data_frame.sample(frac=0.75,random_state=6))

train=data_frame.sample(frac=0.75,random_state=6)
print(train)
test=data_frame.loc[~data_frame.index.isin(train.index),:]
print(test)