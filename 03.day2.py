# %s -- 字符串的位置
# %d -- 整形的位置
# %% -- 转义

# one = input("第一个：")
# two = input("第二个：")
# three = input("第三个：")
# six = input("第四个：")

# msg = """
# 这是第一个输出单元：%s
# 这是第二个输出单元：%d
# 这是第三个输出单元：%s
# 这是第四个输出单元：%s
# """%(one,int(two),three,six)

# print(msg)
##----------------------------------------------------------------------
#扩展  f - strings  (python3.6以上版本的才有)

# name = input("姓名：")
# addr = input("地址：")
# email = input("邮箱：")
#
# msg = f"""
# 这应该就是你姓名了吧：{name}
# 你家地址肯定就是这个：{addr}
# 我连你的邮箱也知道：{email}
# """
# print(msg)

# s = "alexdsb"
# # print(s[1:3])
# print(s[-3:-1])
# print(s[-1:-7:-2])


num = "123456789"
print(num[1])
print(num[0:2])
print(num[7:8+1])
print(num[-2:])
print(num[7])