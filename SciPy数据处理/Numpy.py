import numpy as np
# aArray = np.array([(1,2,3),(4,5,6)])
# print(aArray)
# bArray = np.ones([3,4])
# print(bArray)
#
# x = np.array([(1,2,3),(4,5,6)])
# print(x.ndim)
# print(x.shape)
# print(x.size)
# print(x[:,[0,1]])
# print(x.reshape(3,2))
A = np.array([[1,3,4,2],[5,3,1,6],[7,2,5,4]])
print(A)
print(A.size)
print(A.shape)
print(A.ndim)
B = A.reshape(2,6)
print(B)
B = B + 1
print(B)
# C = np.arange(0,1,0.1)
# print(C)
# D = np.linspace(0,1,12)
# print(D)
# print(B[0:2,1:2])
E = np.arange(1,10)
print(E)
F = E.reshape(3,3)
print(F)
F[1,2] = F[1,2] + 2
print(F)
sum = F.sum()   #总和
print(sum)
sum1 = F.sum(axis=0)    #列和
print(sum1)
sum2 = F.sum(axis=1)    #行和
print(sum2)
max = F.max()   #最大值
print(max)
max1 = F.max(axis=0)    #列最大
print(max1)
min2 = F.min(axis=1)    #列最小
print(min2)
min = F.min()   #最小值
print(min)
mean = F.mean() #平均值
print(mean)
var = F.var()   #方差
print(var)
std = F.std()   #标准差
print(std)



# x = np.array([[1,2],[3,4]])
# r1 = np.linalg.det(x)   #求行列式
# print(r1)
# r2 = np.linalg.inv(x)   #求逆矩阵
# print(r2)
# r3 = np.dot(x,x)     #求内积
# print(r3)
