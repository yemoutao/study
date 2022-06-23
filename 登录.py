def func():
    for i in range(3):
        user = input("请输入账号:")
        passwd = input("请输入密码:")
        with open("./info","r",encoding="utf-8") as f:
            for i in f:
                file_user,file_passwd = i.strip().split(":")
                if file_user == user and file_passwd == passwd :
                    return "登录成功"
            else:
                print("输入的账号密码错误，请重新输入！")

func()