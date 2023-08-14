#1. 引入类库
from numpy import random,dot,exp,array

#2. 加载数据
X = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
y = array([[0,1,1,0]]).T

#3. 设置随机权重
random.seed(1)
weights = 2*random.random((3,1))-1 

#4. 循环
for i in range(10000):
    #利用矩阵相乘计算4个z
    z = dot(X,weights) 
        #利用sigmoid函数(激活函数)计算最终的output
    output = 1/(1+exp(-z))
    
    #看看我们计算出来的和实际发生的有多大误差
    error = y - output

    #计算斜率
    slope = output*(1-output)

    #计算增量
    delt = error*slope

    #更新权重
    weights += dot(X.T,delt)
print(weights)