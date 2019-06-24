#!/usr/bin/python
# -*- coding:utf-8 -*-

# #############tuple :元组##############
# 不可被修改的列表

# user_tuple = ('alex', 'erice', 'seven')
#统计参数个数
# user_tuple.count()
#获取参数的索引
# user_tuple.index()
# v1 = user_tuple.count('alex')
# v2 = user_tuple.index('erice')
# print(v1, v2)

################额外: #########
# user_tuple[0]
# user_tuple[0:1]
# user_tuple[0:5:2]

# 元组本身不可修改，但是其中元素有列表等可修改元素，列表里内容允许修改
# user_tuple = ('alex', 'erice',[11, 22, 33] ,'seven')

# 定义元组最后，一定加逗号####
# li = ('alex',)
# print(li)

##### 列表元组互相转换#####
# user_tuple = ('alex', 'erice', 'seven')
# a = list(user_tuple)
# b = tuple(a)
# print(user_tuple)