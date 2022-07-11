
from asyncore import read


# f = open(file="上门服务", mode="r", encoding="utf-8")  # 在路径前面加r可以转义
# # conter2 = f.read()
# # print(conter2)

# # d = f.read(7)  # 读取七个字符串
# # print(d)

# c = f.readline() # 读取第一行的字符串
# print(c)

# w:  1.先清空文件中的字符串 2. 写入对应字符串

f = open("./ont_file","r+",encoding="utf-8")
f.write("这是python文件读写视频中的测试")
print(f.read())
print(f.tell())
f.close()

with open("./ont_file","r",encoding="utf-8") as w, \
    open("./two_file","r",ncoding="utf-8") as w1:
    print(w.read())
    print(w1.read(3))

import os
# os.rename("上门服务","ont_file")  # 重命名
os.rename("上门第二次","two_file")


os.rename("文件读写.py","file_write.py")

f = open("递归.py","w+",encoding="utf-8")
f.write("###   递归")
f.read()
