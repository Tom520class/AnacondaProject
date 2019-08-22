__author__='zhongyue'
import numpy as np
import pandas as pd

# randn函数返回一个或一组样本，具有标准正态分布
f = np.random.randn(6,4)
print(f)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo',})
print(df2)

# 顶部数据前3
print(df.head(3))
# 底部数据后3
print(df.tail(3))
# 显示索引、列和底层
print(df.index)
print(df.columns)
print(df.to_numpy())
print(df2.to_numpy())
# DataFrame.to_numpy() 的输出不包含行索引和列索引

print("4"*6)
print(df)
# describe 显示数据的快速统计摘要
print(df.describe())
# 转置数据：
print(df.T)
# 按轴排序：
print(df.sort_index(axis=1, ascending=False))
# 按值排序：
print(df.sort_values(by='B'))

print("%"*5)
print(df)
# 获取
# 选择一个列，产生一个“Series”
print(df['A'])
# 通过[ ]选择，对行进行切片
print(df[0:3])
print(df['20130102':'20130104'])

# 通过标签获取一行数据 (不包括index)
print(df.loc[dates[0]])
# 通过标签在多个轴上选择数据：
print(df.loc[:,['A','B']])
# 通过标签同时在两个轴上切片
print(df.loc['20130102':'20130104', ['A', 'B']])
# 减小返回对象的大小：
print(df.loc['20130102', ['A', 'B']])
# 获取标量值：
print(df.loc[dates[0], 'A'])
# 快速访问标量(和上面的方法效果相同)：
print(df.at[dates[0], 'A'])
# 通过传递的整数的位置
print(df)
print(df.iloc[3])
# 通过整数切片
print(df.iloc[3:5, 0:2])
# 通过传递整数的列表按位置切片
print(df.iloc[[1,2,4],[0,2]])
# 整行切片：
print(df.iloc[1:3, :])
# 整列切片：
print(df.iloc[:, 1:3])
# 获取具体值：
print(df.iloc[1,1])
# 快速访问标量(等价于之前的方法)：
print(df.iat[1,1])

print("________________")
# 布尔索引
# 使用单个列的值来选择数据：
df1 = df[df.A > 0]
print(df1)

# 从满足布尔条件的DataFrame中选着值
df = df[df > 0 ]
print(df)

# 使用 isin() 方法过滤：
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
df3 = df2[df2['E'].isin(['two', 'four'])]
print(df3)

print("IIIIIIIIIIIII")
# 赋值
# 添加新列将自动根据索引对齐数据
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print(s1)
df['F'] = s1
print(df)
# 通过标签赋值：
df.at[dates[0], 'A'] = 0
# 通过位置赋值：
df.iat[0, 1] = 0
# 使用NumPy数组赋值：
df.loc[:, 'D'] = np.array([5] * len(df))
# 带有where条件的赋值
df2 = df.copy()
df2[df2>0] = -df2
print(df2)