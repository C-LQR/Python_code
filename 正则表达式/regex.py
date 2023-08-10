import re
text = '麦叔身高：178，体重：168，学号：123456，密码：9527'

# #level1 - 固定的字符串 - 确定字符串中是否有123456
# print(re.findall(r'123456',text))

# #level2 - 某一类字符 - 找出所有的单个的数字
# print(re.findall(r'\d',text))
# print(re.findall(r'\D',text))
# print(re.findall(r'\w',text))
# print(re.findall(r'[1-5]',text))
# print(re.findall(r'[高重号]',text))

# #level3 - 重复某一类字符 - 找所有的数字，比如178，168，123456，9527等。
# print(re.findall(r'\d+',text))
# print(re.findall(r'\d?',text))
# print(re.findall(r'\d*',text))
# print(re.findall(r'\d{1,4}',text))

text = '麦叔电话是18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'

# # #leve4 - 组合level2
# print(re.findall(r'\d{4}-\d{8}',text))

# # #leve5 - 多种情况
# print(re.findall(r'\d{4}-\d{8}|1\d{10}', text))

# # #level6 - 限定位置
# text = '18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
# print(re.findall(r'^1\d{10}|^\d{4}-\d{8}', text))
# print(re.findall(r'1\d{10}$|\d{4}-\d{8}$', text))

# # #level7 - 内部约束
# text = 'barbar carcar harhel'
# print(re.findall(r'(\w{3})(\1)', text))

# #====================================================写正则表达式的5个步骤===============================================================
# #1. 确定模式包含几个子模式
# #2. 各个部分的字符分类是什么
# #3. 各个子模式如何重复
# #4. 是否有外部位置限制
# #5. 是否有内部制约关系

text = '随机数字：01234567891，座机1：0571-52152166，座机2：0571-52152188-1234'
print(re.findall(r'\d{3,4}-\d{7,8}-\d{3,4}|d{3,4}-\d{7,8}',text))

