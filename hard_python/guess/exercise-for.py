#基于range对象的循环
# for i in range(5):
#     print(i)

#基于列表list, 元组tuple的循环
# numbers1 = [3,4,5,6,7]
# numbers2 = (3,4,5,6,7)
# for i in numbers1:
#     print(i)

#基于字符串，字典，集合的循环
# name = 'asfsgh'
# for i in name:
#     print(i)

#作业一：
# for  i in range(1,101):
#     if(i % 3 == 0 and i % 5 != 0):
#         print('麦')
#     elif(i % 5 ==0 and i % 3 != 0):
#         print('叔')
#     elif(i % 3 == 0 and i % 5 == 0):
#         print('Hello')
#     else:
#         print(i)

#作业二
# for  i in range(1,101):
#     if(i == 66):
#         break
#     elif(i % 7 == 0):
#         continue
#     elif(i % 3 == 0 and i % 5 != 0):
#         print('麦')
#     elif(i % 5 ==0 and i % 3 != 0):
#         print('叔')
#     elif(i % 3 == 0 and i % 5 == 0):
#         print('Hello')
#     else:
#         print(i)

#嵌套循环
# names = ['zhangsan','lisi','wangwu']
# is_found = False #表示是否找到了
# for name in names:
#     if(is_found):
#         break
#     for n in name:
#         if(n == 's'):
#             is_found = True
#             break
#         print(n)

#显示循环的index和值
# scores = [98,97,95,86,23]
# for order,s in enumerate(scores,start = 1):
#     print(order,s)

#实现自己的可循环类 - 随机数循环
import random
class RandCount:
    def __iter__(self):
        return self #返回遍历器
    def __next__(self):
        r = random.randint(1,10)
        if(r == 9):
            raise StopIteration
        return r

rc = RandCount()
for i in rc:
    print(i)

