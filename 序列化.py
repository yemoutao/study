###   序列化
# 序列化：将一些特殊的数据转换成字符串（字典，列表）
# 反序列化：将字符串转换成一些特殊的数据
#json: 一种数据类型和字典是一模一样的



import json
s = '{"alex":"dasb"}'
new_s = json.loads(s)  #json.loads 将字符串转换成字典
print(new_s,type(new_s))  #反序列

dic  = {"key":1}
dis = json.dumps(dic)  #json.dumps 将字典转换成字符串
print(dis,type(dis),type(dic))

yunwei = {"运维":"叶涛"}
ops = json.dumps(yunwei,ensure_ascii=False)  #ensure_ascii=False 默认以编码形式去显示，这个参数不以编码显示
print(ops)