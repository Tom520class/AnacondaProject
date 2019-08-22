__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Series计算可以计算加减乘，例为加法
s1 = Series([1,2,3], index=['B','C','D'])
s2 = Series([4,5,6,7], index=['B','C','D','E'])
# 没有的数据为nan
print(s1 + s2)


# DataFrame计算，可加减乘
df1 = DataFrame(np.arange(4).reshape(2,2), index=['A','B'], columns=['BJ', 'GZ'])
print(df1)

df2 = DataFrame(np.arange(9).reshape(3,3), index=['A','B','C'], columns=['BJ','GZ','SH'])
print(df2)
print(df1+df2)

# DataFrame相关函数
df3 = DataFrame([[1,2,3],[4,5,np.nan],[7,8,9]], index=['A','B','C'],columns=['c1','c2','c3'])
print(df3)
# 列和
print(df3.sum())
# 行和
print(df3.sum(axis=1))

# 最大值与最小值
print(df3.max())
print(df3.max(axis=1))
print(df3.min())
print(df3.min(axis=1))

# describe描述
print(df3)
print(df3.describe())