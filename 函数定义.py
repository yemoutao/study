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


def func(*args):    # 在形参的位置上输入 * 是聚合元组 打包、
    print(args)     # *args :  接收多余的位置参数

func(1,2,3,4,5,6,7,5,4,3)



def func(a,b,c,d,**args):   # **value 接收多余的关键字参数
    print("这个是测试",a,b,c,d,args)

func(a=1,b=2,c=3,d=3,f=5,g=6)


def func(*args,**kwargs):
    print(args,kwargs)

func(1,2,4,5,6,6,4,34,5234,a=22,b=4444,c=33)


# 参数的优先级 ： 位置 > 动态位置 > 默认 > 动态关键字



# 名称空间
# 内置空间 ：存放python自带的内容
# 全局空间 ： py文件
# 局部空间 ：函数体中的空间
# 加载顺序： 内置 > 全局 > 局部
# 取值的顺序： 局部 > 全局 > 内置


# 作用域
# 全局作用域： 内置空间 + 全局空间
# 局部作用域： 局部空间
# 函数体中不能修改全局作用域的变量，除非通过申明(global)来修改


hs_version = 100
def func():
    global hs_version     # 申明修改全局作用域的变量
    hs_version = hs_version - 10 
    print(hs_version)

func()

print(hs_version)