import random
import string
# 应用场景：随机复杂密码
lst2 = [str(i) for i in range(10)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
new_lst = random.sample(lst2,k=3)
fzpaswwd = "".join(new_lst)
print(fzpaswwd)

num = [str(i) for i in range(10)]   #数字1-0
xxzm = [chr(i) for i in range(65,91)]
dxzm = [chr(i) for i in range(97,123)]
num1 = random.sample(num,k=1)
xxzm1 = random.sample(xxzm,k=1)
dxzm1 = random.sample(dxzm,k=1)
sjzm =  random.sample('ASDFGHJKLZXCVBNMQWERTYUIOPabcdefghijklmnopqrstuvwxyzzyxwvu1234567890qponmlkjihgfedcba',8)
passwdnum =num1 + xxzm1 + dxzm1 + sjzm 
sjpasswd = "".join(passwdnum)
print(sjpasswd)



ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 11))
print(ran_str)
print(ran_str.__len__)