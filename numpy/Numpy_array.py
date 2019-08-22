import  numpy as np
# 一、 创建一个一维的数组
array = np.arange(20)
print(array)
# 数组的维度
print(array.shape)


# 创建一个二维数组
array = np.arange(20).reshape(4,5)
print(array)
# 数组的维度
print(array.shape)



# 创建三维数组及更多维度
array = np.arange(27).reshape(3,3,3)
print(array)
# 检查它是否是三维数组
print(array.shape)

print("$"*6)
# 其他Numpy函数

# 1   zeros函数创建一个填充零的数组
zer = np.zeros((2,4))
# 2   ones函数创建一个填充了1的数组。
one = np.ones((3,4))
# 3   empty函数创建一个数组。它的初始内容是随机的，取决于内存的状态。
em = np.empty((2,3))
print(em)

# 4   full函数创建一个填充给定值的n * n数组。
fu = np.full((2,2), 3)
print(fu)
# 5   eye函数可以创建一个n * n矩阵，对角线为1s，其他为0。
ey = np.eye(3,3)
print(ey)
# 6   函数linspace在指定的时间间隔内返回均匀间隔的数字。 例如，下面的函数返回0到10之间的四个等间距数字
lin = np.linspace(0,10,num=5)
print(lin)



print("@"*6)

# 二、 从Python列表转换
array = np.array([4,5,6])
print(array)
list = [4,5,6]
print(list)

array = np.array(list)
print(array)


# 使用特殊的库函数

# 创建一个填充0到1之间随机值的数组
rad = np.random.random((2,2))
print(rad)





print("%"*3)
A = np.array([[1,-1,2],[3,2,0]])
print(A)
# 向量:只是具有单列的数组
v = np.array([[2],[1],[3]])
print(v)
# 改为转置行向量
v1 = np.transpose(np.array([[2,1,3]]))
print(v1)


A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b = np.transpose(np.array([[-3,5,-2]]))
print(A)
print(b)
x = np.linalg.solve(A,b)
print(x)
