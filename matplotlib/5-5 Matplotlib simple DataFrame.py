__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt


# pandas绘图之DataFrame


figx,ax = plt.subplots(4,2)
df = DataFrame(np.random.randint(1,10,40).reshape(10,4),columns={'A', 'B','C','D'})
print(df)
# kind='bar'是柱形图，默认为line
df.plot(ax=ax[0][0],kind='bar')
# 横柱形图
df.plot(ax=ax[0][1],kind='barh')
# stacked=True堆叠
df.plot(ax=ax[1][0],kind='bar', stacked=True)
df.plot(ax=ax[1][1],kind='area')
# 画一行
df.iloc[5].plot(ax=ax[2][0])
# 画10行
for i in df.index:
    df.iloc[i].plot(ax=ax[2][1],label=str(i))
# 画一列
df['A'].plot(ax=ax[3][0])
# 转置画行
print(df.T)
df.T.plot(ax=ax[3][1])
plt.show()