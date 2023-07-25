#5大金刚：list, tuple, str, set, dictionary

#8字口诀：建-增删改查操-切复

#=======8钟玩法========
#1. 创建
#建1
names = []
#建2
names = list() #可以接受一个iterable的对象

#2. 增添元素
#增1
names.append('maishu')
#增2
names.insert(0,886)
#增3
names.extend([1,0,2])

#3. 删除元素
#删1:根据下标删除，根据内容删除
del names[1]
#删2:默认删除最后一个，也可以指定删除下标，返回删除的元素
names.pop(0)
#删3:只会删除第一个，没有符合条件的，会抛出ValueError
#names.remove('maishu')

#4. 改元素
names[1] = 'biaoshu'


#5. 查询元素
#查1
print(names[1])

#6. 操作元素
#操1：loop，遍历
for i in names:
    print('hello', i)

for index,n in enumerate(names):
    print(f'no {index+1} is {n}')

#操2：基本运算: + , * , ==
scores = [87,65,98,32]
print(names + scores) #与extend是一样的效果
print(scores*3)
print(names == scores)

#操3：排序 orderde sorted
# list.reverse() 会修改原列表
# reversed(list) 不会修改原列表，返回一个新的
# sort同上
# sort可以指定reverse=Ture
# sort可以指定key
print(scores)
scores.reverse()
print(scores)

scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)

print(sorted(scores))
print(sorted(scores,reverse=True))

name_scores = [('zhangsan',87),('maishu',100),('lisi',98)]
print(sorted(name_scores, key = lambda n:n[1]))

#操4：max，min，sum
print(max(scores))
print(min(scores))
print(sum(scores))

#6. 切片操作 start:end:step
print(names[::])

#7. 复：推导式，map，filter
nums = list(range(100))
print(nums)

sq_nums = [n*n for n in nums]
print(sq_nums)
nums_3 = [n for n in nums if n%3==0]
print(nums_3)

print(list(map(lambda n:n*8, nums)))