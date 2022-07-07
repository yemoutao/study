###   装饰器：  在不修改源代码及调用方式的前提下，额外增加新的功能
###   开发封闭原则：1.对额外新增的功能开发
#                  2.对源代码及调用方式是封闭
#                  3.

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

# 标准版装饰器
 