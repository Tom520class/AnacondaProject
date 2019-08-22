__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# 方法1：直接赋值法
df1 = DataFrame(np.arange(9).reshape(3,3), index=['北京','上海','广州'], columns=['A','B','C'])
print(df1)
df1.index =Series(['bj','sh','gz'])
print(df1)


# 方法2：map
print(df1)
print(df1.index.map(str.upper))
df1.index = df1.index.map(str.upper)
print(df1)

# 方法3：rename
print(df1)
df1.rename(index=str.lower, columns=str.lower)
print(df1.rename(index=str.lower, columns=str.lower))
print(df1)
print(df1.rename(index={'BJ': '北京'}, columns={'A':'a'}))


# 自定义map函数处理dataframe
print(df1)

def test_map(x):
    return x+'ABC'


print(df1.index.map(test_map))
print(df1.rename(index=test_map))