import sys #系统模块
import time #时间模块

def input_limit():
    try:
        guess_limit = int(sys.argv[1])#最多猜测次数
    except ValueError: #异常处理模块
        guess_limit = 4 #默认为4次
        print('输入次数有误,使用默认值:4')
    return guess_limit

def calc_time(begin_time):
    end_time = time.time()
    used_time = end_time - begin_time
    used_time = round(used_time,2) #保留小数点后2位
    print(f'共用时{used_time}秒')
    return used_time

def print_score(scores):
    best_score = min(scores,key=lambda x:x[2] if x[1] else 9999)
    print('==========战绩==========')
    for _cycle, _is_right, _used_time in scores:
        best_label = '最好' if (_cycle == best_score[0] and best_score[1]) else '' #设定最好的标志
        if (_is_right):
            label = '胜利'
        else:
            label = '失败'
        print(f'第{_cycle}轮,{label},用时{_used_time}秒 {best_label}')
    print('========================')