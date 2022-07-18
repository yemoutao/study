###   random模块(随机数)



from random import random
print(random())  # 0~1 随机小数

import random
print(random.randint(1,10))   #在1-10整数区间取随机数
lst = [1,23,3,4,5,6563,5,5]
print(random.choice(lst))     #在lst列表的字符串取随机数
print(random.choices(lst,k=2)) #在lst列表的字符串取两个随机数，取的两个值有重复值
print(random.sample(lst,k=2)) #在lst列表的字符串取两个随机数，取的两个值没有重复值

lty = [1,2,3,4,6,7,8]
random.shuffle(lty)    # 洗牌，打乱顺序
print(lty)

# 应用场景：验证码
lst2 = [str(i) for i in range(10)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
new_lst = random.sample(lst2,k=6)
s = "".join(new_lst)
print(s)
