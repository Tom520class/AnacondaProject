__author__ = 'zhongyue'

import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt


# matplotlib简单绘图之subplot



# 等差数列50个值
x = np.linspace(0.0,5.0)
# 生成两个y轴坐标
y1 = np.sin(np.pi*x)
y2 = np.sin(np.pi*x*2)
# 画线
# plt.plot(x,y1,'b--', label='sin(pi*x')
# plt.ylabel('y1 value')
# plt.plot(x,y2,'r--', label='sin(pi*2x')
# plt.ylabel('y2 value')
# plt.xlabel('x value')
# plt.title('this is x-y value')
# 显示线的label
# plt.legend()
# plt.show()



# 使用subplot画子图
# 两行一列的图，第三个参数为第几个图
# plt.subplot(2,1,1)
# # 画线
# plt.plot(x,y1,'b--',label='y1')
# plt.ylabel('y1')
# # 切换到第二个子图
# plt.subplot(2,1,2)
# # 画线
# plt.plot(x,y2,'r--',label='y2')
# plt.ylabel('y2')
# plt.xlabel('x')
# plt.legend()
# plt.show()




# 两行两列
# plt.subplot(2,2,1)
# 画线
# plt.plot(x,y1,'b--',label='y1')
# plt.ylabel('y1')
# # 切换到第二个子图
# plt.subplot(2,2,2)
# # 画线
# plt.plot(x,y2,'r--',label='y2')
# plt.ylabel('y2')
# plt.xlabel('x')
# plt.subplot(2,2,3)
# plt.plot(x,y1,'b*', label='y3')
# plt.legend()
# plt.show()




# subplots

# a = plt.subplots()
# print(type(a))

figure, ax = plt.subplots(2,2)
print(figure)
# ax是一个数组，可以通过ax访问子图
print(ax)
ax[0][0].plot(x,y1)
ax[0][1].plot(x,y2)
plt.show()