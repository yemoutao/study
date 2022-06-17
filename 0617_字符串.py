
num = input("请输入需要加的数字：")
addnum = num.split(" ")
print(addnum)
print(int(addnum[0]) + int(addnum[1]))




num1 = input("请输入数字：")
addnum1 = num1.split("+")
delnum1 = num1.split("-")
twonum = addnum1[1].split("-")
# print(twonum1)
# print(addnum1)
# print(delnum1)
# print(twonum)
print(int(addnum1[0]) + int(twonum[0]) - int(delnum1[1]))