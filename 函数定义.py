#  只有函数被调用的时候，函数其中的代码才会执行。
#  写函数实现功能，其实是给功能加上一个外壳。
#  调用函数： 函数名+()
#  函数定义的时候，函数体中存放的是代码
#  返回和显示是有很大的区别，返回的内容还可以继续使用，显示的就无法进行使用。
#  函数执行完，函数体中开辟的空间就自动销毁。


from distutils.log import debug
from itertools import count
from telnetlib import theNULL


s = ["1","2","3","4"]
def my_len():
    count = 0
    for i in s:
        count += 1
    return count    #返回值返回给函数的调用部分

c = my_len()
print(c + 15)

my_len()  #  调用函数： 函数名+()

def test():
    print("这是第一条")
    print("这是第二条")
    return "返回第一","返回第二"

t = test()
print(t)


