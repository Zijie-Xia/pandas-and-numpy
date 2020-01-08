# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:22:57 2019

@author: 74787
"""

import pandas as pd
df1=pd.DataFrame({'id':[100,101,102],'color':['red','blue','red']},columns=['id','color'],index=['a','b','c'])
print(df1)

df2=pd.DataFrame([[100,'red'],[101,'blue'],[102,'red']],columns=['id','color'])
print(df2)

import numpy as np
arr=np.random.rand(4,2)
arr=pd.DataFrame(arr,columns=['one','two'])
print(arr)

df3=pd.DataFrame({'student':np.arange(100,110,1),'test':np.random.randint(60,101,10)})
print(df3)
df3=df3.set_index('student')
print(df3)

s=pd.Series(['round','square'],index=['c','b'],name='shape')
print(s)
df4=pd.concat([df1,s],axis=1)
print(df4)