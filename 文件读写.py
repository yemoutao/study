
from asyncore import read


f = open(file="上门服务", mode="r", encoding="utf-8")
# conter2 = f.read()
# print(conter2)

d = f.read(6)
print(d)