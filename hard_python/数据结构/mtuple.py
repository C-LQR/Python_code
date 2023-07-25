# 掌握5大金刚之tuple,和8字口诀：基建-增删改查操-切复
# 5大金刚包括：list，tuple，set，dict，str

#基本概念：tuple是一个有序的，不可改的数据结构immutable
l = [5,2,3]
t = (5,2,3)
#优点：1.快 2.安全 3.元组可以作为dict的key
#python -m timeit '(1,2,3)' 用了9ns左右
#python -m timeit '[1,2,3]' 用了65ns左右
#用的地方：1.参数 2.其他不变的情况

#建
t1 = (5,8,9)
t2 = tuple([5,8,9])
t3 = tuple('maishu')
t4 = (5,)
t5 = ()
print(type(t5))
print(t1,t2)


#增 - 不能

#删 - 不能

#改 - 不能 

#查
a = (1,3,5)
print(a[0])

#操 - 不能

#切
b = a[1:3]
print(b)

#复
c = a[:]
print(c)