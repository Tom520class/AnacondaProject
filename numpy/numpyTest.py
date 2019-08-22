__anthor__ = 'zhongyue'
# Numpy入门

import numpy as np

my_array = np.array([1,2,3,4,5])
# 类型
print(type(my_array))
# 数组
print(my_array)
# 包含几个元素的数组
print(my_array.shape)
# 取值
print(my_array[0])
# 指定索引值更新值
my_array[1] = -1
print(my_array)


my_new_array = np.zeros((5))
print(my_new_array)

my_random_array = np.random.random((5))
print(my_random_array)

my_2d_array = np.zeros((2,3))
print(my_2d_array)
print(my_2d_array.shape)


my_2d_new_array = np.ones((2,4))
print(my_2d_new_array)


my_array = np.array([[1,2,5],
                     [3,4,6]])
# 索引1行和索引0列中的元素
print(my_array[1][0])

my_array_colum_2 = my_array[:,1]
my_array_colum_3 = my_array[1,:]
# 只取1列所有的值
print(my_array_colum_2)
# 只取1行所有的值
print(my_array_colum_3)


# 2-4 数组与矩阵运算
a = np.array([[1.0, 2.0],
              [3.0, 4.0]])
b = np.array([[5.0, 6.0],
              [7.0, 8.0]])
sum = a + b
difference = a-b
product = a * b
quotient = a/b
print(sum)
print(difference)
print(product)
print(quotient)



maxtrix_product = a.dot(b)
print(maxtrix_product)



# 数组基础切片定义
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
# 多维数组切片
print(a[2,4])
print(a[0,1:4])
print(a[1:4, 0])
print(a[::2,::2])
print(a[:, 1])


# 数组属性
print(type(a))
print(a.dtype)
print(a.size)
print(a.shape)
# itemsize属性是每个项占用的字节数
print(a.itemsize)
# ndim 属性是数组的维数
print(a.ndim)
# nbytes 属性是数组中的所有数据消耗掉的字节数。
print(a.nbytes)

# 数组特殊运算符
# 所有元素相加
print(a.sum())
# 最小元素
print(a.min())
# 最大元素
print(a.max())
# 第一个元素和第二个元素相加，
# 并将计算结果存储在一个列表中，
# 然后将该结果添加到第三个元素中，
# 然后再将该结果存储在一个列表中。
# 这将对数组中的所有元素执行此操作，
# 并返回作为列表的数组之和的运行总数。
print(a.cumsum())


# 花式索引:获取数组中我们想要的特定元素的有效方法。
a = np.arange(0,100,10)
indices = [1,5,-1]
b = a[indices]
print(a)
print(b)


# 布尔屏蔽:它允许我们根据我们指定的条件检索数组中的元素。

import matplotlib.pyplot as plt
a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a,b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <=np.pi / 2)
plt.plot(a[mask],b[mask], 'go')
# plt.show()


# 缺省索引:不完全索引是从多维数组的第一个维度获取索引或切片的一种方便方法

a = np.arange(0,100, 10)
b = a[:5]
c = a[a >= 50]
print(b)
print(c)


# Where 函数根据条件返回数组中的值的有效方法
a = np.arange(0,100, 10)
b = np.where(a < 50)
c = np.where(a >= 50)[0]
print(b)
print(c)

a = np.array([2,4,4])
b = np.array([[3],
             [2],
              [4]])
print(a.dot(b))


print("%"*5)
# 2-5 Array的input和output
# 重点放在genfromtxt函数上
# genfromtxt考虑到缺失值的情况


# 定义输入:
#   genfromtxt的唯一强制参数是数据的来源。
# 它可以是一个字符串，一串字符串或一个生成器



# 将行拆分为列:delimiter
# delimiter关键字用于定义拆分应该如何进行。
import numpy as np
from io import BytesIO

data = '1,2,3\n4,5,6'
a = np.genfromtxt(BytesIO(data.encode()), delimiter=",")
print(a)


data = "  1  2  3\n  4  5 67\n890123  4"
b = np.genfromtxt(BytesIO(data.encode()), delimiter=3)
print(b)

data = "123456789\n   4  7 9\n   4567 9"
c = np.genfromtxt(BytesIO(data.encode()), delimiter=(4,3,2))
print(c)

# autostrip参数
# 默认情况下，当一行被分解为一系列字符串时，单个条目不会被剥离前导空白或尾随空白。
# 通过将可选参数autostrip设置为值True，

data = "1, abc, 2\n 3, xxx, 4"
d = np.genfromtxt(BytesIO(data.encode()), delimiter=",", dtype='1S5')
print(d)

d1 = np.genfromtxt(BytesIO(data.encode()), delimiter=",", dtype='1S5', autostrip=True)
print(d1)

# comments参数
# 可选参数comments用于定义标记注释开始的字符串。
# 默认情况下，genfromtxt假定comments='#'。
# 这种行为有一个明显的例外：如果可选参数names=True，则会检查第一条注释行的名称。
data = """#
    # Skip me !
    #  Skip me too !
    1, 2
    3, 4
    5, 6 #This is the third line of the data
    7, 8
    # And here comes the last line
    9, 0
    """
t = np.genfromtxt(BytesIO(data.encode()), comments="#", delimiter=",")
print(t)

print("#"*4)
# 跳过直线并选择列
#skip_header和skip_footer参数
# 文件中存在标题可能会妨碍数据处理。
# 在这种情况下，我们需要使用skip_header可选参数。
# 此参数的值必须是一个整数，与执行任何其他操作之前在文件开头跳过的行数相对应。
# 同样，我们可以使用skip_footer属性跳过文件的最后一行n，并给它一个n的值

data = "\n".join(str(i) for i in range(10))
s = np.genfromtxt(BytesIO(data.encode()),)
print(s)
s1 = np.genfromtxt(BytesIO(data.encode()), skip_header=3, skip_footer=5)
print(s1)

# usecols参数
# 在某些情况下，我们对数据的所有列不感兴趣，但只有其中的一小部分。
# 我们可以用usecols参数选择要导入的列。
# 该参数接受与要导入的列的索引相对应的单个整数或整数序列。
# 请记住，按照惯例，第一列的索引为0。
# 负整数的行为与常规Python负向索引相同。

data = '1 2 3\n 4 5 6'
s2 = np.genfromtxt(BytesIO(data.encode()), usecols=(0, -1))
print(s2)
s3 = np.genfromtxt(BytesIO(data.encode()), names="a,b,c", usecols=("a", "c"))
print(s3)