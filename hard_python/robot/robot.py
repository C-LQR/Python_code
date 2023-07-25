#引入另一个文件/模板
import opening as open
import order

#1. 出场
open.icon()

#2. 了解主人：问问题
name = open.ask()

#终端退出死循环：ctrl + c
while(True):
    print('-------------------------')
    print('小麦:您有什么吩咐？')
    cmd = input('我:')
    if(cmd == 'time'):
        #4. 显示时间
        year = order.show_time_v2().year
        #5. 判断是否为闰年
        order.run_nian(year)
    elif(cmd == 'hello'):
        #3. 问好
        open.hello(name)
    elif(cmd == '88'):
        print('小麦:88,有事再找我！')
        break
    elif(cmd == 'tianqi'):
        order.tianqi('宜春')
    else:
        print(order.ai_talk(cmd))




