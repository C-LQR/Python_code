# 目地：将一段文本以词云形式展示

# 如何做：
#       1.你需要在第14行：txt="____" ,下划线处填入你需要分析的文本
#       2.你需要在第22行：wc.to_file("____"),下划线处填入图片名称，(文件扩展名：jpg/png都可)，图片文件自动创建在当前目录下
#       3.其他地方代码不要动

# author：LQR
# date：2023/03/25

from jieba import *
from wordcloud import *

txt = ""
word_list = lcut(txt) #精确分词：将字符串分词返回一个列表，包括标点符号
# print(word_list)

newtxt = " ".join(word_list) #列表元素空格拼接成字符串
# print(newtxt)

wc = WordCloud(font_path="msyh.ttc",background_color="white").generate(newtxt) #font_path="msyh.ttc"非常重要，不设置图片显示不出中文，同时也不用考虑字符串中的标点符号
wc.to_file("") # to_file("xxx.png")：参数不能传绝对路径