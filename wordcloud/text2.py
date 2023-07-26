from jieba import *
from wordcloud import *

txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规定组织、计算机指令，使计算机能够自动进行各种运算处理。。。。。。。。"
word_list = lcut(txt) #精确分词：将字符串分词返回一个列表，包括标点符号
print(word_list)

newtxt = " ".join(word_list) #列表元素空格拼接成字符串
print(newtxt)

wc = WordCloud(font_path="msyh.ttc",background_color="white").generate(newtxt) #font_path="msyh.ttc"非常重要，不设置图片显示不出中文，同时也不用考虑字符串中的标点符号
wc.to_file("词云.jpg") # to_file()：参数不能传绝对路径