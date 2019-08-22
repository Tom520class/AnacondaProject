__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

# 数据分组技术GroupBy

df = pd.read_csv('../data/city_weather.csv')
print(df.head())
print(len(df))
# 按照city这一列进行分组
print(df.groupby(df['city']))
# 通过groupby方法指定列进行分组，最后得到一个DataFrameGroupBy 类型的对象，可以对这个对象进行后续的操作
g = df.groupby(df['city'])
print(g.groups)
# 它返回了根据city分组后的所有的组，以及这个组所在的索引值。

# 查看某一个分组:get_group可以指定一个分组的名称查看一个分组的具体信息
print(g.get_group('BJ'))
# 分组计算
# 求平均值
df_bj = g.get_group('BJ')
print(df_bj.mean())
print(g.mean())
# 最大最小值
print(g.max())
print(g.min())
# 分组对象转化为列表和字典
print(list(g))
print(dict(list(g)))
print(dict(list(g))['BJ'])

# 遍历DataFrameGroupBy对象中的数据
for name,group_df in g:
    print(name)
    print(group_df)


# GroupBY = Split+Apply+Combine












