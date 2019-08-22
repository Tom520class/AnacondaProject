__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt



# matplotlib简单绘图之Series


# plt.subplot(4,2,1)
#
# # cumsum()函数演示
s = Series([1,2,3,4,5])
# print(s.cumsum())
#
s1 = Series(np.random.randn(1000)).cumsum()
# # kind参数是修改画图类型
# s1[:10].plot(kind='bar')
#
#
# plt.subplot(4,2,2)
# # 设置title，grid网格线,还有线的类型style
# s1.plot(kind='line', grid=True,label='S1',title='This is Series', style='--')
# # plt.legend()
# # plt.show()
#
#
# plt.subplot(4,2,3)
# # 绘制两个Series
# s1.plot(kind='line', grid=True, label='S1', title='This is Series', style='--')
s2 = Series(np.random.randn(1000)).cumsum()
# s2.plot(label='S2')
# plt.legend()
# plt.show()


# 使用subplots


# fig, ax = plt.subplots(2,1)
# s1.plot(ax=ax[0], label='S1')
# s1.plot(ax=ax[1], label='S2')
# plt.legend()
# plt.show()

fig, ax = plt.subplots(2,1)
s1[0:10].plot(ax=ax[0], label='S1', kind='bar')
s2.plot(ax=ax[1], label='S2')
plt.legend()
plt.show()