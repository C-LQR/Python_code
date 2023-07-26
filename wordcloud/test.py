from wordcloud import *
txt = "I like Python.I am learning Python"
wc = WordCloud(background_color="white").generate(txt)
wc.to_file('test.png')