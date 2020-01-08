# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:55:35 2019

@author: 74787
"""

import sys 
import pandas as pd

input_file=sys.argv[1]
data_frame=pd.read_csv(input_file,error_bad_lines=False)

print(data_frame.info())
#more accurate
print(data_frame.info(memory_usage='deep'))

print(data_frame.memory_usage())
print(data_frame.memory_usage(deep=True))

#how to save space and speed up computations
print(sorted(data_frame['Supplier Name'].unique()))
data_frame['Supplier Name']=data_frame['Supplier Name'].astype('category')
print(data_frame['Supplier Name'])
print(data_frame['Supplier Name'].cat.codes)
print(data_frame['Supplier Name'].cat.categories)
print(data_frame.memory_usage(deep=True))

df=pd.DataFrame({'ID':[100,101,102,103],'quality':['good','very good','good','excellent']})
print(df)
print(df.sort_values('quality'))
df.quality=df.quality.astype('category',categories=['good','very good','excellent'],ordered=True)
print(df)
print(df.sort_values('quality'))
print(df.loc[df.quality>'good',:])