###   time模块

import time


#time 时间分类：
# 1. 时间戳           - - 程序员做计算
print(time.time())    # 时间戳
# 2. 结构化时间       - - 程序员查看   -- > 1657781261.372803
print(time.localtime())   #将时间戳转换称为结构化时间
# 3. 字符串时间       - - 给用户查看的 -- > yyyy.dd.mm
t = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S",t))  #将时间戳转换为字符串

str_time = "2022-7-14 17:18:04"
t_time = time.strptime(str_time,"%Y-%m-%d %H:%M:%S")   # 将字符串时间转换成结构化时间
time.mktime(t_time)         #将字符串转换为时间戳




### datetime

from datetime import datetime

print(datetime.now())  # 显示字符串时间
print(datetime.timestamp(datetime.now()))  # 时间对象转换成时间戳
print(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")) # 时间对象转换成字符串
