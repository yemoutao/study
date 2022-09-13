from importlib.util import set_package
from re import S


# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

class myclass:
    """简单的class实例"""
    i = [1,2,3,4,5,6,7]
    list = ['ops:323','dev:221']
    def f(self):
        s = round(6)
        return print(s)

x = myclass()

# print(x.f())
print(x.list)
print(myclass().f())
# print(globals())


class ops():
    #定义class的基本属性：
    name = ''
    gender = ''
    age = 0
    #定义初始化构造方法：
    def __init__(self,n,a,s):
        self.name = n
        self.gender = a
        self.age = s
    def speak(self):
        print("%s是一名%s,年龄为%d"%(self.name,self.gender,self.age))



class ymt(ops):
    grade = ''
    def __init__(self, n, a, s, w):
        ops.__init__(self,n,a,s)
        self.grade = w
    def speak(self):
        print("%s是一名%s,年龄为%d,工作主要是%s的 " %(self.name,self.gender,self.age,self.grade))

f = ymt('yemt','男生',18,'222')
f.speak()
