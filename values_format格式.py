
# 索引传参
soft1 = "{}是一个数据存储,可以对{}持久化存储"
test1 = soft1.format("linux","Mysql")
print(test1)

# 关键字传参
soft2 = "{soft}是一个CICD流程,可以对{system}进行自动化部署"
test2 = soft2.format(soft="Rocketmq",system="linux")
print(test2)


# 容器传参 -- 选择项传入变量
soft3 = "{0[1]}是一个中间件，可以对{1[0]}进行消息转发"
test3 = soft3.format(["mysql","Rocketmq","Jenkins"],["liunx","windows","unix"])
print(test3)



####
# 字符串的格式化format

# (1)顺序传参
# (2)索引传参
# (3)容器类型传参

# format 字符串填充符号的使用["^","<",">"]
# ^ 字符串居中
# < 字符串居左
# > 字符串居右
# 10填充的个数(原字符串+填充字符 一共10个)


req = """
1.登录系统
2.注册账号
3.注销账号
"""
print(req)

test = "请输入账号:{number:*<9}"
user = test.format(number="271283046")
print(user)

test1 = "你知道访问的系统为{req:~>7}"
head = test1.format(req="教训系统")
print(head)

test2 = "欢迎你登录{sucess:!<6}"
body = test2.format(sucess="成功")
print(body)



