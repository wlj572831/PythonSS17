#!/usr/bin/python
# -*- coding:utf-8 -*-

#1. while 循环输入 1 2 3 4 5 6 8 9 10
# i = 1
# while i < 11:
#     if i == 7:
#         pass
#     else:
#         print(i)
#     i += 1

#2. 求1-100的所有数的和
#while
# i = 1
# value = 0
# while i < 101:
#     value = value +i
#     i += 1
# print(value)

# for
# value = 0
# for i in range(1,101):
#     value += i
# print(value)

#3.输出1-100内的所有奇数
# i = 1
# while i < 101:
#     if i%2 == 0:
#         pass
#     else:
#         print(i)
#     i += 1

#4.输出1-100内的所有偶数
# i = 1
# # while i < 101:
# #     if i%2 == 0:
# #         print(i)
# #     i += 1

#5.求1-2+3-4+5...99的所有数的和
# i = 1
# # value = 0
# # while i < 100:
# #     if i%2 == 0:
# #         value -= i
# #     else:
# #         value += i
# #     i += 1
# # print(value)

#6.用户登陆(三次机会重试)
# user_name = 'alex'
# pwd = 'dba'
# i = 1
# while i < 4 :
#     name_ = input('>>>用户名：')
#     pwd_ = input('>>>密码：')
#     if user_name == name_ and pwd == pwd_:
#         print('yes!')
#     else:
#         print('sorry,已输错:%s次' %i)
#     i += 1