###   多个装饰器装饰一个函数
###   先执行离被装饰的函数最近的语法糖

def wrapper(func):
    def inner(*args,**kwargs):
        print("第一个装饰器开始")
        ret = func(*args,**kwargs)
        print("第一个装饰器结束")
        return ret
    return inner

def wrapper2(func):
    def inner1(*args,**kwargs):
        print("第二个装饰器开始")
        ret = func(*args,**kwargs)
        print("第二个装饰器结束")
        return ret
    return inner1

def wrapper3(func):
    def inner3(*args,**kwargs):
        print("第三个装饰器开始")
        ret = func(*args,**kwargs)
        print("第三个装饰器结束")
        return ret
    return inner3

@wrapper   # foo = wrapper(foo)
@wrapper2  # foo = wrapper2(foo)
@wrapper3  # foo = wrapper3(foo)
def foo():
    print("xiao pa cai")

foo()