# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:10:45 2019

@author: 74787
"""

import sys 
import pandas as pd
import matplotlib.pyplot as plt

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.groupby('Supplier Name')['Part Number'].mean())

print(data_frame.groupby('Supplier Name').mean())

print(data_frame[data_frame['Supplier Name']=='Supplier X']['Part Number'].mean())

print(data_frame.groupby('Supplier Name')['Part Number'].max())

print(data_frame.groupby('Supplier Name')['Part Number'].min())

print(data_frame.groupby('Supplier Name')['Part Number'].agg(['count','min','max','mean']))

#%matplotlib inline
plt.plot(data_frame.groupby('Supplier Name').mean())
plt.show()

