__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# 通过apply进行数据预处理
df = pd.read_csv('../data/apply_demo.csv')
print(df.head())
print(df.size)

# 使用apply进行预处理
# apply可以批量的改变dataframe中的数据。
s1 = Series(['a']*5)
df['A'] = s1
print(df)
print(df.size)
# 将A列改的值为大写
df['A'] = df['A'].apply(str.upper)
print(df)


# data列拆分
# data列的值其实是三个部分组成：
# Symbol、Seqno、Price
# .strip()是去除空格，split（" "）是以空格为分隔符进行分割
print(df['data'][0].strip().split(' '))

def foo(line):
    item = line.strip().split(' ')
    return Series([item[1],item[3],item[5]])

# 然后对原dataframe的data列数据进行apply处理：
# df = pd.read_csv('../data/apply_demo.csv')
print(df)
df_tmp = df['data'].apply(foo)
df_tmp = df_tmp.rename(columns={0:'Symbol',1:'Seqno',2:'Price'})
print(df_tmp.head())

# 将新的dataframe连接到原来的dataframe中并删除data列数据，得到最终的结果：
df_new = df.combine_first(df_tmp)
print(df_new.head())
del df_new['data']
print(df_new.head())
df_new.to_csv('../data/demo_duplicate.csv')