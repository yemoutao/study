###   装饰器：  在不修改源代码及调用方式的前提下，额外增加新的功能
###   开发封闭原则：1.对额外新增的功能开发
#                  2.对源代码及调用方式是封闭
#                  3.@wrapper  语法糖
#    装饰器的应用场景：1. 面向对象对象
#                     2. 登录认证
#                     3.falsk路由全都是有参数装饰器

from os import rename
import time


def func():
    print("this is 装饰器")

def foo():
    print("THIS IS 装饰器")


def run_time(f):
    def inner():
        start_time = time.time()
        f()
        # time.sleep(2)
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
      #  """执行被装饰函数前"""
         func(*args,**kwargs)
      #  """执行被装饰函数后"""
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
def hero(hero_name,hero_title):
    ret = print(f"选择{hero_name}出战，{hero_title}")
    return ret

# hero(hero_name="亚索",hero_title="死亡如风，常伴吾身")
hero("小学生之手","懦弱之举，我绝不姑息")


# 有参数的装饰器
def auth(arg):      # auth(arg) == auth(100)
    def wrapper(func):    #1.func() == tb(100)
        def inner(*args,**kwargs):     # tb(100) == inner(100)
            if arg:
                print("开始装饰")
                ret = func(*args,**kwargs) # ret = tb(100)
                print("装饰成功")
            else:
                print("装饰失败")
                ret = func(*args,**kwargs) # ret = tb(100)
            return ret                 # return "lv"
        return inner
    return wrapper

@auth(100)   #语法糖 == auth(100) -->  tb = auth(100)(tb) --> tb = auth(100)(tb)
def tb(money):
    print(f"花了{money}：卖了一个皮包")  #print("花了100：卖了一个皮包")
    return "lv"

# tb = wrapper(tb)
tb(100)    # auth(100)tb(100)


# 多层参数装饰器套用
def foo(aa):   # aa = 5
    def auth(arg):     # arg = False
        def wrapper(func):   # func = tb(100)
            def inner(*args,**kwargs):
                if arg:
                    print("开始装饰")
                    ret = func(*args,**kwargs)
                    print("装饰成功")
                else:
                    print("装饰失败")
                    ret = func(*args,**kwargs)
                return ret
            return inner
        return wrapper
    return auth

fee = foo(5)
@fee(False)   # == fee(5)auth(False)tb
def tb(money,beizhu):
    print(f"花了{money}块钱：{beizhu}")

tb("1","卖出了一颗棒棒糖")   # == fee(5)auth(False)tb(100)
