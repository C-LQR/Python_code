import time
from datetime import datetime
import requests
import json

def show_time_v1():
    #格式：今天是：2023年1月5日 16:21:32
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec
    print(f'今天是：{year}年{month}月{day}日 {hour}:{minute}:{second}') 

def show_time_v2():
    dt = datetime.now()
    #print(f'今天是：{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}')
    print(dt.strftime('小麦:今天是:%Y年%m月%d日 %H:%M:%S'))
    return dt

# 判断是否为闰年
def run_nian(year):
    year = int(year)
    if (year % 4 == 0): 
        if (year % 100 != 0):
            print(f'小麦:{year}年是是闰年呢！')
        elif (year % 100 == 0 and year % 400 == 0 ):
            print(f'小麦:{year}年是闰年呢！')
        else:
            print(f'小麦:{year}年不是是闰年哦！')

    else:
        print(f'小麦:{year}年不是闰年哦！')

# 早期“人工智能”
def ai_talk(question):
    return question.replace('你','我').replace('不','').replace('吗','').replace('?','!').replace('？','!')

def tianqi(city):
    url = 'http://t.weather.sojson.com/api/weather/city/101240501'
    res = requests.get(url)
    tq_text = res.text
    tq_json = json.loads(tq_text)

    wendu = tq_json['data']['wendu']
    shidu = tq_json['data']['shidu']
    pm25 = tq_json['data']['pm25']
    quality = tq_json['data']['quality']

    print(f'{city}：温度是{wendu}℃ ,湿度是{shidu} ,pm2.5是{pm25} ,空气质量是{quality}')