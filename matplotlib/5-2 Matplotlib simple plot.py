import timeit

__author__ = 'zhongyue'

import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt



# matplotlib简单绘图之plot



a = [1,2,3]
# # 传入a为x轴，y轴默认
# plt.plot(a)
# plt.show()
a = [1,2,3]
b = [4,5,6]
# # 传入a为x轴，b为y轴
# plt.plot(a,b)
# plt.show()

#计算计算运行时间

# 修改画出来的图表的样子， *号
# plt.plot(a,b,'*')
# 红色的虚线
# plt.plot(a,b,'r--')
# 蓝色的虚线
# plt.plot(a,b,'b--')
# 传入两个图表
c = [10,8,6]
d = [1,8,3]
# plt.plot(a,b,c,d)
# plt.plot(a,b,c,d,'*')
# plt.plot(a,b,'b--',c,d,'r*')
# plt.show()

# 画一个正弦函数
t = np.arange(0.0,2.0,0.1)
print(t.size)
s = np.sin(t*np.pi)
# plt.plot(t,s,'r--')
# plt.show()

# 画两条线，并设置x,y轴的label和title
# plt.plot(t,s,'r--', t*2, s, '--')
# plt.xlabel('this is x')
# plt.ylabel('this is y')
# plt.title('this is a demo')
# 需要有图例的名字才能显示
# plt.legend()
# plt.show()

# 设置每个图的label
plt.plot(t,s,'r--', label='aaa')
plt.plot(t*2,s,'--', label='bbb')
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('this is a demo')
# 需要label名字显示
plt.legend()
plt.show()








# x = np.linspace(0,2*np.pi,100)
# print(x)
# y = np.sin(x)
# print(y)
# plt.plot(x,y)
# plt.show()

