__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn简单画图(二) -- 直方图和密度图


# 使用matplotlib
plt.subplot(4,2,1)
s1 = Series(np.random.randn(1000))
plt.hist(s1)

plt.subplot(4,2,2)
s1.plot(kind='kde')
plt.show()

# Seaborn
# 同时绘制密度图和直方图
plt.subplot(4,2,1)
sns.distplot(s1, hist=True,kde=True)
plt.subplot(4,2,2)
sns.distplot(s1,hist=True,kde=False,rug=True)
plt.subplot(4,2,3)
sns.distplot(s1,bins=20,hist=True,kde=False,rug=True,color='k')
# 绘制密度图的另一种方法，shada阴影填充
plt.subplot(4,2,4)
sns.kdeplot(s1,shade=True,color='r')
plt.show()