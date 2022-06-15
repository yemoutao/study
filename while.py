#模拟qq登录
#
# user_1 = input("账号：")
# passwd_1 = input("密码：")
#
# if user_1 == "alex" and passwd_1 == "alex12":
#    print("登录成功")
# else:
#   print("账号密码错误")


# num =0
# while num < 100:
#       print("该数字已经在",num)
#       num = num +1
#       if num == 9:
#           print("数字到9")
#           continue


msg = """
1.登录
2.注册
3.查看账号
4.查看密码
"""
while True:
    print(msg)
    user_com = input("请输入选项：")
############################################################选择一
    if user_com == "1":
        print("如没注册请回退上一级")
        while True:
            user_name = input("username:")
            passwd = input("passwd:")
            if user_name == zc_user and passwd == zc_passwd:
                print("登录成功")
                break
            else:
                print("账号密码错误")
                user_age = input("返回上一级请输入n:")
                if user_age == "n":
                    break
#############################################################选择二
    if user_com == "2":
        zc_user = input("username:")
        zc_passwd = input("passwd:")
        print(zc_user,"账号注册成功")
#############################################################选择三
    if user_com == "3":
        print("你的账号是：",zc_user)

#############################################################选择四
    if user_com == "4":
        user_sum = 1
        while user_sum < 4:
            cat_user = input("请输入你要查看密码的账号：")
            if cat_user == zc_user:
                print("你的密码是：",zc_passwd)
            elif cat_user != zc_user:
                print("没有这个账号！")
                user_sum = user_sum +1


