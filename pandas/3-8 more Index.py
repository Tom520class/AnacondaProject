__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Pandas多级Index


# Series的多级Index
s1 = Series(np.random.randn(6), index=[['1','1','1','2','2','2'],['a','b','c','a','b','c']])
print(s1)
print(type(s1['1']))
print(s1['1']['a'])
print(s1[:, 'a'])

# 1.此时的Series是二维的数据结构
# 2.可以将它转换成DataFrame
df1 = s1.unstack()
print(df1)
df2 = DataFrame([s1['1'], s1['2']])
print(df2)

#将DataFrame再转换回Series
s2 = df1.unstack()
print(s2)
s2 = df1.T.unstack()
print(s2)


# DataFrame的多级Index
df = DataFrame(np.arange(16).reshape(4,4))
print(df)
df = DataFrame(np.arange(16).reshape(4,4),
               index=[['a','a','b','b',],[1,2,1,2]],
               columns=['A','B','C','D',])

print(df)
df = DataFrame(np.arange(16).reshape(4,4),
               index=[['a','a','b','b',],[1,2,1,2]],
               columns=[['BJ','BJ','SH','SH'],[8,9,8,8]])
print(df)
print(df['BJ'])
print(df['SH'])
print(df['BJ'][8])
