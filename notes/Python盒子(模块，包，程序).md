5.3  模块和import语句

模块是同路径不带.py的另一个python文件名.

例子：import test
    # -- 引用test模块中的所有代码
    #只要在名称前面加test. test.py的所有文件都对主程序可见。
    #通过模块名称限定模块的内容，可以避免命名冲突。
    #其他模块可能也会有同命名的的函数，这样做不会被错误的调用。
    #如果调用次数少使用内部调用方式，调用次数多使用外部调用方式。

内部调用：
def get_description():
    import test
    possibilities = ['rain','snow','sleet','fog']
    return test.choice(possibilities)

外部调用：
import test
def get_description():
    possibilities = ['rain','snow','sleet','fog']
    return test.choice(possibilities)

5.3.2 使用别名导入模块 >> import test as step

5.3.3 导入模块的一部分 >>
                        from test import get_description #导入test模块中的get_description函数
                        from test import get_description as alis #导入test模块中的get_description函数并设置别名为alis

5.3.4 模块搜索路径  >>

import ss
for place in sys.path:
    print(place)

5.5.1 使用seetdefault()和defaultdict()处理缺失的键




table_valut = {'mysql': 5, 'system': 1}
print(table_valut)
intvault = table_valut.setdefault('redis', 9)
print(table_valut)

##5.5.2 Counter 计数器

from collections import Counter
breakfast = ['spam','spam','eggs']
breakfast_counter = Counter(breakfast)
breakfast_counter

# 函数most_common()以降序返回所有元素，如果有指定一个数字，会返回该数字前面的的元素

breakfast_most = breakfast_counter.most_common(1)
breakfast_most

lunch = ['eggs','eggs','bacon']
lunch_counter = Counter(lunch)
lunch_counter

# 两个相加，重叠的会取最大值的那个
breakfast_counter + lunch_counter
# 两个相减，重叠的会取最小值的那个
breakfast_counter - lunch_counter
lunch_counter - breakfast_counter

# '&' 会取集合中的共同项
breakfast_counter & lunch_counter

5.5.3 使用有序字典OrderedDict()按键排序
从一个迭代器按照相同的顺序返回，试着用元组(键，值)创建一个有序字典
DM:
from collections import OrderedDict
qotues = OrderedDict([
    ('More','A wise  guy,huh?'),
    ('Larry','Ow'),
    ('Curly','welcome me '),
])

for stooge in qotues:
    print(stooge)

输出：
More
Larry
Curly

5.5.4 双端队列：栈+队列 （deque）
deque 是一种双端队列，同时具有栈和队列的特征，可以从序列的任何一端添加和删除项。
函数popleft()去掉最左边的项并返回该项。
函数pop()去掉最右边的项并返回该项。
从两边一直向中间扫描，只要两端的字符匹配，一直弹出直到到达中间：
DM：
def  palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palindrome('saa')
输出：
>>> palindrome('saa')
False
>>> palindrome('sas')
True

5.5.5 使用itertools迭代代码结构 -- > 在for ... in 循环中调用迭代函数，每次会返回一项，并记住当前调用的状态。
chain()参数是一个单数迭代对象，也会使用参数进行迭代。
DM:
import itertools as it
for item in it.chain(['a','b'], ['1','2']):
    print(item)
>>>a
>>>b
>>>1
>>>2
# cycle() 是一个在它的参数之间循环的无限迭代器
import itertools as it
for item in it.cycle([1,2]):
    print(item)
>>>1
>>>2
...
