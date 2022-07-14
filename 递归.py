###   递归

# 递： 一直传参
# 归： 返回

# 递归的最大深度（层次）官方说明1000 实际测试 998/997

#   1.不断调用自己本身  （无效递归 -- 死递归 ）
#   2.有明确的终止条件

#无效递归

# def func():
#     print(1)
#     func()
# func()

def age(n):
    if n == 3:
        return 38
    return age(n+1)-2

def age1(n):
    if n == 3:
        return 38
    return age(n+1)-2

def age2(n):
    if n == 3:
        return 38
    return age1(n+1)-2

print(age2(1))

lst = ["ansiw","alex",'jordan',["anni","buke",["kobe"]],'test']
def foo(m):
    for i in m:
        if type(i) == list:
            foo(i)
        else:
            print(i)
foo(lst)