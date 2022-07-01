#   函数的第一类对象及使用



def func():
    print(2)

list = [func,func,func]
for i in list:
    i()


def foo(a):
    print(a)    #  print(3)
    return 1

def f1(b):
    ret = foo(b)   # 返回 1
    return 2

def func(c):
    f1(c)          # 返回 2

# 没写返回值默认调用return返回None

ret1 = func(3)
print(ret1)       # 输出 None

# 不管在什么位置，只要是函数名()就是在调用这个函数
# 谁调用的函数就把返回值返回给谁

def foo(a):
    print("is foo")
    return a()   # a() == a1


def f1():
    print("is f1")
    return "执行F1"

def func(c,b):
    return c(b)

ret1 = func(foo,f1)
print(ret1)


foo(f1)


a = 18
def func(a):
    a = a + 1
    def foo(a):
        print(a)
    foo(a)

func(a)

def func():
    a = 10
    def foo():
        a = 5
        def f1():
            print(a)
            return "123"
        ret = f1()
        return ret
    print(a)
    foo()
ret = func()
print(ret)