__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


# Seaborn简单画图(四) -- 设置图形显示效果

x = np.linspace(0,14,100)
y1 = np.sin(x)
y2 = np.sin(x+2)*1.25
def sinplot():
    plt.plot(x,y1)
    plt.plot(x,y2)

sinplot()
plt.show()

# axex_style and set_style

sns.set()
sinplot()
plt.show()

# seaborn提供可绘图的5种风格主题：’darkgrid’, ‘dark’, ‘white’, ‘whitegrid’, ‘ticks’
style = ['white','dark','whitegrid','darkgrid','ticks']
sns.set_style(style[0])
sinplot()
plt.show()


sns.set_style(style[1])
sinplot()
plt.show()

# 可以通过字典设置风格
sns.axes_style()
print(sns.axes_style())


# 设为网格线颜色,之后再使用这个主题，边框颜色都会变成红色。
sns.set_style(style[3], {'grid.color':'red'})
sinplot()
plt.show()


print(sns.axes_style())
# 恢复默认的风格参数:清空设置
sns.set()
print(sns.axes_style())




# plotting_context() and set_context()
# 设置图形比例
# seaborn预设了四种线条风格：’paper’, ‘notebook’, ‘talk’, ‘poster
context = ['paper', 'notebook','talk','poster']
sns.set_context(context[3])
sinplot()
plt.show()


print(sns.plotting_context())
# 设置网格线宽度
sns.set_context(context[1], rc={'grid.linewidth':3.0})
sinplot()
plt.show()
print(sns.plotting_context())

sns.set()
print(sns.plotting_context())