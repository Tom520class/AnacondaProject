__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


# Seaborn简单画图(一) -- 散点图


# 打开一个花瓣长宽数据文件
iris = pd.read_csv('../data/iris.csv')
print(iris.head())
# 绘制的颜色字典,zip传入俩个列表
print(iris.Name.unique())
color_map = dict(zip(iris.Name.unique(),['blue','green','red']))
print(color_map)


# 使用matplotlib画图

for species, group in iris.groupby('Name'):
    plt.scatter(group['PetalLength'],group['SepalLength'],color=color_map[species],alpha=0.3,edgecolors=None,label=species)
plt.legend(frameon=True, title='Name')
plt.xlabel('PetalLength')
plt.ylabel('SepaiLength')
plt.show()



# 使用seaborn画图

sns.lmplot('PetalLength','SepalLength', iris,hue='Name',fit_reg=False)
plt.show()