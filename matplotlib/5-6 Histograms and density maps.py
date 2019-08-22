__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt




# 直方图和密度图


plt.subplot(4,2,1)
s = Series(np.random.randn(1000))
# 生成了两个array和一个图形对象，第一个array是在区间数的数量，第二个是区间范围
# hist画直方图,rwidth表示图形宽度
plt.hist(s, rwidth=0.9)


plt.subplot(4,2,2)
a = np.arange(10)
print(a)
plt.hist(a,rwidth=0.9)


plt.subplot(4,2,3)
# bins默认10，分割区间,orientation修改为水平的，color修改颜色，
plt.hist(s,rwidth=0.9, bins=20, color='r', orientation='horizontal')


plt.subplot(4,2,4)
# kde画密度图
s.plot(kind='kde')

plt.show()