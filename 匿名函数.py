# 匿名函数: 没有真实名字或者没有名字的函数，也叫一句话函数


from re import X


# 定义结构：
# lambda value_nm: nm -- >  lambda  形式参数 ： 实参（相当于函数的return返回值）

nm = lambda x,y : x - y
print(nm(65,3))

f = lambda x : x[-3:]
print(f([1,2,45,6,7,8,90,4]))