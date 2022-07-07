### 推导式
# 1. 编写一些有规律性

lst = []
for i in range(1,11):
    lst.append(i)
    print(lst)

# 普通循环模式
print([i for i in range(1,11)])

# 筛选模式
print([i for i in range(1,11) if i > 3]) # i变量为一体，判断语句为一体：先执行判断语句再赋值给变量，判断语句中从左到右去执行。
#                                          结构：[结果  for循环  条件]
#                                               [三元运算 for循环 条件]

print([i if i > 3 else "not can" for i in range(1,7)])


# 字典推导式：        集合是{i，i}  字典是{i:1...}
print({i:i for i in range(5)})

#元组没有推导式

#生成器表达式
g = ((i for i in range(5)))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

