# 内置函数

from multiprocessing.sharedctypes import Value
from tracemalloc import start


1.abs()  # 绝对值

2.format() # 格式化值 或 转换进制

3.value.strip()  # 删除前导和尾随空格的字符串副本

4.enumerate()  # 枚举(差不多相当于遍历)
        lst = ["yemt","yzz","xiaojg"]
        for i in enumerate(lst):
            print(i)

        lst = ["yemt","yzz","xiaojg"]
        for i in enumerate(lst,1):    # enumerate(lst,1) 参数中的1是属于起始位，从第一位开始数起
            print(i)

5. float() # 浮点型
        print(float(10))

6.sum()   # 求和   sum([相加的值]，起始的值)
        ggt = sum([12,4,5,76,7,6545,3], 456465)
        print(ggt)


7.type()  # 查询类型
        print(type(ggt))

8.zip() # 拉链式合并字符串
        lst1 = [1,2,3,45,4]
        lst2 = [3,4,5,23,1]
        print(dict(zip(lst1,lst2)))  # 字典的创建方式，lst1函数和lst2中的值交替拉链显示

        d = dict(a=1,balu=2)   # 字典的创建方式
        print(d)

9.dir()   # 查看当前内容具有什么方法
        print(dir(str))


10.print()  # 打印

11.reverse()  # 反向排序


# sed="" = 分隔符
# end="" = 结尾
# file="" = 输入到文件


# 不常用的内置函数以下：


1. all()  # 判断里边的元素是否都为真，返回值为布尔值
        print(all([1,3,4,3,6,7,8]))

2.any()  # 判断里边的元素是否有一个为真，返回的是布尔值 or
        print(any([1,3,0,set()]))

3.callable()  # 判断里面的函数是否可被调用
        def func():
            return "被调用"
        print(callable(func))

4.divmod() # 商余
        print(divmod(5,3))

5.frozenset()  # 冻结集合

6.globals()  # 查看全局变量值

7.hash()  # 需要都是可变数据才能拿到值

8. oct()  # 将十进制转换为八进制

9. pow()  # 幂运算


