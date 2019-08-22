__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
# 添加index
s1 = Series([1,2,3,4], index=['A','B','C', 'D'])
print(s1)

print(s1.reindex(index=['A','B','C', 'D', 'E']))

print(s1.reindex(index=['A','B','C', 'D', 'E'], fill_value=10))
s2 = Series(['A','B','C'], index=[1,5,10])
print(s2)

print(s2.reindex(index=range(15)))

print(s2.reindex(index=range(15), method='ffill'))

# 当reindex时指定的index少于原有的index的情况
print(s1)
print(s1.reindex(index=['A','B']))

# drop删除指定index值
print(s1)
print(s1.drop('A'))
print("{{{{{{{{{{{{{{{{{}}}}}}}}}}}")





# dataframe的reindex
# 改变dataframe的index和column：
df1 = DataFrame(np.random.rand(25).reshape([5,5]), index=['A','B','D','E','F'], columns=['c1','c2','c3','c4','c5'])
print(df1)
print(df1.reindex(index=['A','B','C','D','E','F']))
print(df1.reindex(columns=['c1','c2','c3','c4','c5','c6']))

# 同时改变dataframe的index和column：
print(df1.reindex(index=['A','B','C','D','E','F'], columns=['c1','c2','c3','c4','c5','c6']))


# 当reindex时指定的index少于原有的index的情况：
print(df1)
print(df1.reindex(index=['A', 'B']))

# dataframe的drop操作
print(df1)
print(df1.drop('A', axis=0))
print(df1.drop('c1', axis=1))
# axis为0表示指定的变量是index，axis为1表示指定的变量为列

