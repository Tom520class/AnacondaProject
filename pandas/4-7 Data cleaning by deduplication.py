__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# 通过去重进行数据清洗
df1 = pd.read_csv("../data/demo_duplicate.csv")
print(df1)
del df1['A']
del df1['Unnamed: 0']
print(df1)


# Seqno列去重

# 查看Seqno列都有哪些值
print(df1['Seqno'].unique())
# 这是去除重复后，这一列中都包含的值。
print(len(df1['Seqno'].unique()))

# duplicated方法
# duplicated用于从上到下比较指定某一列的值，当这个值第一次出现时，返回False，当这个值和上一个比一样时，返回True
print(df1['Seqno'].duplicated())
# 通过这个方法就可以查看到这一列中重复的情况

# drop_duplicates去重复
print(df1['Seqno'].drop_duplicates())
# drop_duplicates方法将会把这一列duplicated方法结果中为True的项删除，False的项保留

# 这样从结果看是按照一行四个元素的一致性去重的，而不是按照Seqno这一列的值去重
print(df1.drop_duplicates())

# 指定按照Seqno这列的值去重
print(df1.drop_duplicates(['Seqno']))



# keep参数
# 在不指定keep的时候，它的值默认为first，表示如果有多个重复的则保留第一个。也可以指定其他的值
print(df1.drop_duplicates(['Seqno'], keep='last'))
# 这里就是指定当有多个重复的时候保存最后一个
