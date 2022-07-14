###   自定义模块

# 1. 拿来主义，拿来使用就可以，能用即可
# 2. 以文件的形式管理代码

# 模块分类:
# 1.自定义模块
# 2.内置模块(标准库)
# 3.第三方模块(类库)


# 5.3  模块和import语句

# 模块是同路径不带.py的另一个python文件名.

# 例子：import test
#     # -- 引用test模块中的所有代码
#     #只要在名称前面加test. test.py的所有文件都对主程序可见。
#     #通过模块名称限定模块的内容，可以避免命名冲突。
#     #其他模块可能也会有同命名的的函数，这样做不会被错误的调用。
#     #如果调用次数少使用内部调用方式，调用次数多使用外部调用方式。



# 5.3.2 使用别名导入模块 >> import test as step

# 5.3.3 导入模块的一部分 >>
#                         from test import get_description #导入test模块中的get_description函数
#                         from test import get_description as alis #导入test模块中的get_description函数并设置别名为alis

# 模块导入顺序：内存 > 内置 > sys.path


from inspect import modulesbyfile
import  闭包 as t

print(t.fot()(1))
print(t.ret(1))

import sys
print(sys.path)

import sys
sys.path.append("F:\python\study")  #添加默认模块路径
print(sys.path)


import sys
print(sys.modules)  # 查看内存中所有的模块

# 模块安装和用途
# # # pip install module(模块名)
