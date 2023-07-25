import time
robot_name = '小麦'

def icon():
    print('''
         \_/
        (* *)
       __)#(__
      ( )...( )(_)
      || |_| ||//
   >==() | | ()/
       _(___)_
      [-]小麦[-]''')
    time.sleep(1)

def hello(name):
    print(f'小麦:你好，{name}，我是{robot_name}')
    print(f'小麦:{name}，吃饭了吗？')
    print(f'小麦:我对{name}的敬仰之情，犹如滔滔黄河之水，一发而不可收拾！') 
    time.sleep(1)
    
    #转义字符
    #print('what\'s your name')

    #自己查文档：print文档查询
    # print(10,end=' ')
    # print(20,end=' ')
    # print(30,end=' ')

def ask():
    name = input('小麦:我是小麦，你叫什么名字？\n我:')
    age = input('小麦:我8岁了,你呢？\n我:')
    #类型转化
    age = int(age)
    
    if (age < 30):
        if (age < 12):
            print(f'小麦:{age}岁是小P孩!和我一样!')
        else:
            print(f'小麦:你才{age}啊!')
            print('小麦:你真年轻，如花似玉的年龄!')

    elif (age < 50):
        print(f'小麦:你{age}了')
        print('小麦:我喜欢成熟的人的魅力!')

    else:
        print(f'小麦:你{age}了')
        print('小麦:丰富的人生阅历，让你更有魅力！')

    time.sleep(1)
    return name
    

