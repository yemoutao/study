from functools import reduce


1.filter()    # --- 过滤，可迭代对象
        lst = [1,3,4,5,6]
        def func(x):
            return x < 5
        print(list(filter(func,lst)))

        print(list(filter(lambda x:x<5,lst)))

        lst_name = [{'id':1,'name':'yemt','age':16},
                    {'id':1,'name':'yzz','age':19},
                    {'id':1,'name':'xjg','age':20}]

        print(list(filter(lambda x:x["name"] == "yemt",lst_name)))
        print(list(filter(lambda x:x["age"] != "16",lst_name)))


2. map()   # -- 映射   map(函数，可迭代对象)
        lst_str = [1,3,4,5,6]
        print(list(map(lambda x:str(x),lst_str)))  --精简版：   print(list(map(str,lst)))


3.sorted()  # 排序   sorted(可迭代对象，key=排序规则)
        lst_len_name = ['呼伦贝尔','汕头','连云港','深圳']
        print(sorted(lst_len_name, key=len))

        dic = {'a':1,'b':2,'c':3}
        print(sorted(dic.values()))

        lst_name = [{'id':1,'name':'yemt','age':16},
                    {'id':2,'name':'yzz','age':19},
                    {'id':3,'name':'xjg','age':20}]

        print(sorted(lst_name,key=lambda x:x["id"],reverse=False))  #reverse=False 获取的值排序，reverse=Ture  获取的值反向排序

4.max()   #求最大值
        print(max(1,2,3,4,5,6788,65))
        print(max([1,2,3,4,5,-6788,65],key=abs))
        print(max([1,2,3,4,5,-6788,65],key=str))  #str是根据ascii码位来比较的

5.min()  #求最小值
        print(min(1,2,3,4,5,6788,65))

6.reduce() #累计计算
        lst = [1,3,4,5,6]
        from functools import reduce
        def func(x,y):
            return x * y
        print(reduce(func,lst))   #1*3=3,3*4=12,12*5=60,60*6=360

