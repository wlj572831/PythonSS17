#!/usr/bin/python
# -*- coding:utf-8 -*-


################ range #############
# range(@a, @b, @c)
# @a 开始值 @b 结束值 @c 步长

## 关于range
#1. 3.x  中，range(1,10) 不会立即创建，循环时才会创建
#   2.x 中 range(1,10) 会立即创建, xrange(1,10)循环时才会创建

# # 单个参数
# for i in range(10):
#     print(i)
# # 两个参数
# for i in range(1, 10):
#     print(i)
# 三个参数
# for i in range(1,10,2):
#     print(i)

li = ['alex', 'eric', 'rain']

# 输出序列和参数
# for i in range(len(li)):
#     print(i , li[i])

########## enumerate ##############

# 循环输出列表的索引值和元素值
# for i,value in enumerate(li,100):
#     print(i+100,value)