#掌握5大金刚之string,和9字口诀：基建-增删改查操-切复
#5大金刚包括:list,tuple,str,set,dict

#======================================================================
#A. 基 - 1. 是一个字符序列（sequence）, 2. 基于uft-8编码 3. str
#编码：1. ASCII码 2. ISO-9995-1 3. ANSI 4. GBK 5. UTF-8
# name = '张三'
# print(name)

#小练习：给一个字符串，找出里面所有的o的字符个数
# obj_str = 'adfhgoqwuironfoiiqnhfo'
# num_of_o = 0
# for i in obj_str:S
#     if (i == 'o'):
#         num_of_o += 1
# print(f'字符串"{obj_str}"里面所有的o字符个数是{num_of_o}')

#======================================================================
#B. 建
# -简单建
zs = '张三'
ls = "李四"
ww = '''王五'''
print(ww)

# - 转移字符,引号的相互嵌套
zs = '张\t三'
ls = 'lisi\'s'
print(zs)
print(ls)

# - 构造方法
score = 98.99
score_str = str(score)
print(score_str)

#小练习：用一个字符串，打印出’静夜思‘这首诗
poetry='''
    静夜思
        -李白
    床前明月光，
    疑是地上霜。
    举头望明月，
    低头思故乡。
    '''
print(poetry) 

#======================================================================
#C. 增 - 不能更改

#======================================================================
#D. 删 - 不能更改

#======================================================================
#E. 改 - 不能更改

#======================================================================
#F. 查
# -可以通过下标来访问一个字符
shame = '打工是不可能的！'
print(shame[1])

# -字串是否存在 - membership: in,not in
#identity: is, not is
print('可能' in shame)
print(type(shame ) is str)

# -开头，结尾
print(shame.startswith('打工'))
print(shame.endswith('！'))

# -所在的下标
print(shame.index('可能'))

#小练习：定义一个字符串的list，里面保存了很多名字，找出所有姓张的人
names = ['张三','李四','王五','赵六','张二麻子']
for name in names:
    if(name[0] == '张'):
        print(name) 
 
#======================================================================
#G. 操
# -格式化
name = 'zhangsan'
print(f'hello,{name}!')

#拆分
names = '张三,李四,王五,赵六,二麻子'
for n in names.split(','):
    print(n)

#合并
names2 = ['张三','李四','王五']
print('-'.join(names2))

#查找：出现的次数，RE
name = '我是一只小小小小小小小鸟'
print(name.count('小'))

#改变大小写
zhangsan = 'zhang san is a bad guy'
print(zhangsan.title())
print(zhangsan.capitalize())
print(zhangsan.upper())
print(zhangsan.lower())
print(zhangsan.swapcase())
print(zhangsan.isupper())
print(zhangsan.islower())

#运算
name8 = ' wangba '
print(name8 + name)
print(name8 * 8)

#去空格
print(name8.strip())
print(name8.lstrip())
print(name8.rstrip())

#查漏补缺 - 替换
print(name.replace('小','大'))

#查漏补缺 - 比较
print('maishu' > 'z')
print('z'>'Z ')

#小练习：自行研dir(str)里面的每个方法的作用  查文档-命令行：1. py  2. dir(str)
#======================================================================
#H. 切片

#======================================================================
#I. 复制 - 不可更改

#======================================================================

#10个字符串练习

