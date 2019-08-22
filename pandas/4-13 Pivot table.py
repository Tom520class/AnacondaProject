__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

# 透视表
df = pd.read_excel('../data/sales-funmel.xlsx')
print(df)

# 生成透视表
# 默认情况: 透视表的方法是：pivot_table
print(pd.pivot_table(df,index=['Name']))

# 指定聚合的方法:通过参数aggfunc指定聚合的方法
print(pd.pivot_table(df,index=['Name'], aggfunc='sum'))
# 可以看到，还是Trantow-Barrows这一行，现在他的price和Quantity都是原始数据的和。

# 按多个index生成透视表
print(pd.pivot_table(df, index=['Name', 'Rep','Manager']))
print(pd.pivot_table(df, index=['Manager','Rep']))

# 指定显示的列:除了index，还可以通过values参数来制定显示哪些列：
print(pd.pivot_table(df, index=['Manager','Rep'], values=['Price']))

# 指定column
print(pd.pivot_table(df, index=['Manager','Rep'], values=['Price', 'Quantity'], columns=['Product']))
# 可以看到在price和quantity下，又根据product把它们再次细分。


# 有一些NaN的值，可以通过参数fill_value进行填充：
print(pd.pivot_table(df, index=['Manager','Rep'], values=['Price', 'Quantity'], columns=['Product'], aggfunc='sum', fill_value=0))