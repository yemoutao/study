###   迭代器

# 可迭代对象; 1. 能被for循环，循环的就是可迭代对象
        #    2. 具有__iter__() 方法就是可迭代对象

s = "alex"
# lst = []
lst_1 = {}

#可迭代对象具有__iter__()方法

s.__iter__()
# lst.__iter__()
lst_1.__iter__()

#迭代器：具有__iter__()和__next__()方法
lst = [1,2,3,4,5,6]
new_lst = lst.__iter__()   #将迭代对象转换为迭代器
print(new_lst.__next__())  #从迭代器中取值



# 迭代器的优点： 节省空间 -- 惰性进制 （可以被for循环）
# 迭代器的缺点： 使用不灵活，一次性的，不可逆

t = [1,2,3,4,5,6,7,8,9]
t1 = t.__iter__()
while True:
    try:                      #尝试
        print(t1.__next__())  #尝试着运行一下
    except StopIteration:     #异常捕捉
        break


