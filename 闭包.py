#coding:utf-8

# 闭包： 函数的嵌套， 1.使用非全局变量
#                   2.且不是本层变量
#                   3.就是闭包
# 为什么要学习闭包： 闭包的作用就是能够保护数据的安全性和干净性
# 闭包的场景： 1.装饰器
#             2.保护数据的安全性

# def foo():
#     lst = []
#     def func(money):
#         lst.append(money)
#         print(sum(lst) / len(lst))
#     return func
# func = foo()
# func(15000)
# func(35000)
# func(55000)
# func(45000)
# func(95000)
# func(15000)


def fot():
    a = []
    def func(num):
        a.append(num)
        print(a)
    return func

ret = fot()
# print(ret(1),ret(2))
ret(1)
ret(2)
ret(3)