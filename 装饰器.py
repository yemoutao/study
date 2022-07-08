###   装饰器：  在不修改源代码及调用方式的前提下，额外增加新的功能
###   开发封闭原则：1.对额外新增的功能开发
#                  2.对源代码及调用方式是封闭
#                  3.@wrapper  语法糖

import time


def func():
    print("this is 装饰器")

def foo():
    print("THIS IS 装饰器")


def run_time(f):
    def inner():
        start_time = time.time()
        f()
        time.sleep(2)
        stop_time = time.time()
        print(f"运行时间为：{stop_time - start_time}")
    return inner

foo = run_time(foo)
foo()

func = run_time(func)
func()

# 标准版装饰器:
def wrapper(func):
    def inner(*args,**kwargs):
        """执行被装饰函数前"""
        func(*args,**kwargs)
        """执行被装饰函数后"""
    return inner

def foo(*args):
    print(*args)

foo = wrapper(foo)
foo(20200020220)



def wrapper(func):    #1.func() == tb()
    def inner(*args,**kwargs):     # tb(100) == inner(100)
        ret = func(*args,**kwargs) # ret = tb(100)
        return ret                 # return "lv"
    return inner

@wrapper  #语法糖 == tb = wrapper(tb)

def tb(money):
    print(f"花了{money}：卖了一个皮包")  #print("花了100：卖了一个皮包")
    return "lv"

# tb = wrapper(tb)
tb(100)


# 语法糖
def wrapper(func):
    def inner(*args,**kwargs):
         start_game()
         func(*args,**kwargs)
         start_plate()
         end_plate()
         print("你个小趴菜，输了游戏")
    return inner

def start_game():
    ret = print("TIMI")
    return ret

def start_plate():
    ret = print("全军出击")
    return ret

def end_plate():
    ret = print("End Game")
    return ret

@wrapper
def hero(hero_name):
    ret = print(f"选择{hero_name}出战，死亡如风，常伴吾身")
    return ret

hero("亚索")


# 有参数的装饰器
