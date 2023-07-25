#掌握5大金刚之string,和9字口诀：基建-增删改查操-切复
#5大金刚包括:list,tuple,str,set/frozenset,dict

#======================================================================
#A. 基础 - 键值对,key:value, key必须是Immut的对象
s = {'zs':66, 'lisi':88, 'maishu':100}

#======================================================================
#B. 建
s = {'zs':66, 'lisi':88, 'maishu':100}
s = dict() #空的字典
s = dict([(1,99),(2,88),(3,100)]) #包含成对的数据的iterable
print(s)

names = ['zs','lis','ww','wb']
scores = [78,56,78,99]
s = dict(zip(names,scores))
print(s)

s3 = dict.fromkeys(names,19)
print(s3)

#======================================================================
#C. 增
# s['ruhua'] = 89
# print(s)
# s['damei'] = 77
# print(s)

#======================================================================
#D. 删 - del, pop, popitem, clear
# del s['damei'] #如果删除的key不存在，会抛出KeyError
# print(s)

# print(s.pop('ruhua'))
# print(s)

# print(s.popitem())
# print(s)

# s.clear()
# print(s)

#======================================================================
#E. 改
print(s)
s['wb'] = 100
print(s)

#======================================================================
#F. 查 - get, in, not in
print('ww' in s)
print(s['ww'])
print(s)
print(s.get('wwx'))
print(s)

s.setdefault('www','google.com')
print(s['www'])
print(s)

#======================================================================
#G. 操 - 遍历，items,keys,values,sort
for k in s:
    print(k,s[k])

print(s.keys())
print(list(s.keys()))

print(s.values())
print(list(s.values()))

print(s.items())
print(list(s.items()))

s2 = {k:v for k,v in sorted(s.items())}
print(s2)

#======================================================================
#H. 切 - 不存在

#======================================================================
#I. 复 - copy
s4 = s.copy()
print(s4)
print(id(s))
print(id(s4))

s5 = {'dfd':88,'xxx':89,'ww':120}
print(s)
print(s5)
s.update(s5)
print(s)