__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


# Seaborn简单画图(三) -- 柱状图和热力图


# 复制这里的数据（https://github.com/mwaskom/seaborn-data/blob/master/flights.csv）
# sns.load_dataset('flights')
# df = pd.read_clipboard()
# df.to_csv("../data/flights.csv")
df = pd.read_csv("../data/flights.csv")
print(df.head())
# 用透视表转换
df = df.pivot(index='month', columns='year', values='passengers')
print(df)


# 热力图
sns.heatmap(df)
plt.show()

# 按列的折现图
df.plot()
plt.show()

# annot描述
sns.heatmap(df,annot=True)
plt.show()

# fmt设置显示格式
sns.heatmap(df,annot=True,fmt='d')
plt.show()

s = df.sum()
print(s)

# 柱状图
sns.barplot(x=s.index,y=s.values)
plt.show()

s.plot(kind='bar')
plt.show()
