#!/usr/bin/python
#  -*- coding:utf-8 -*-

#创建
user = {
    'name': 'alex',
    'pwd': '123456'
}
#常用操作

#索引获取值
# n = user['name']
# print(n)

#新增或修改
# user['name'] = 'usr_name'

#删除
# del  user['name']

#长度
# a = len(user)
# print(a)

# #循环字典

#只循环key值
# for i in user:
#     print(i)

#只循环key
# for i in user.keys():
#     print(i)

#只循环value
# for i in user.values():
#     print(i)

#循环输出key和value的列表
# for i in  user.items():
#     print(i)

#循环输出key和value
# for key,val in  user.items():
#     print(key, val)

#列表与字典之间的相互嵌套
user_dict = {'a':1,
             'b':2,
             'c':3,
             'd':{'key1':'val', 'key2':'val2', 'key3':'val3'},
             'e':[1,2,3,4]
             }
print(user_dict['e'][1])

