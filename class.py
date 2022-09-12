from importlib.util import set_package
from re import S


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

f = ymt('yemt','男生',18,'搬砖')
f.speak()
