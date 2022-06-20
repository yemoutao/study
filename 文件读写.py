
from asyncore import read


# f = open(file="上门服务", mode="r", encoding="utf-8")  # 在路径前面加r可以转义
# # conter2 = f.read()
# # print(conter2)

# # d = f.read(7)  # 读取七个字符串
# # print(d)

# c = f.readline() # 读取第一行的字符串
# print(c)

# w:  1.先清空文件中的字符串 2. 写入对应字符串

f = open("./测试.txt","r+",encoding="utf-8")
f.write("这是python文件读写视频中的测试")
print(f.read())