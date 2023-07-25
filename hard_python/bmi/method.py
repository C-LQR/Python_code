#函数的3要素：名字，参数，返回值
def bmi(height,weight):
    """"计算BMI的值:
        公式：身高/(体重*体重)
        身高单位：米
        体重单位：千克/公斤
        函数返回计算好的BMI值,保留1位小数
    """
    bmi_value = round(weight/(height*height))
    if (bmi_value < 18.5):
        return bmi_value,'多吃点'
    elif (bmi_value <= 24):
        return bmi_value,'你真棒!'
    else:
        return bmi_value,'多运动'

is_fat = bmi
print(is_fat (1.62,60))
# import random
# for i in range(10):
#     random.randint(1,2)

import hell
hell.sey_hell()



