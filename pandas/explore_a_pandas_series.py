# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:21:53 2019

@author: 74787
"""

import sys 
import pandas as pd
import matplotlib.pyplot as plt

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame['Supplier Name'].describe())

#it is a series
print(data_frame['Supplier Name'].value_counts())

# per cent
print(data_frame['Supplier Name'].value_counts(normalize=True))

#output all Supplier Names
print(data_frame['Supplier Name'].unique())

#output the number of supplier names
print(data_frame['Supplier Name'].nunique())

#output the number of different SupplierNames and Cost
print(pd.crosstab(data_frame['Supplier Name'],data_frame.Cost))

plt.plot(pd.crosstab(data_frame['Supplier Name'],data_frame.Cost))
plt.show()

