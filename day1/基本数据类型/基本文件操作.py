#!/usr/bin/python
#  -*- coding:utf-8 -*-

#1.打开并读取文件内容
# f1 = open('db', 'r')
# data = f1.read()
# f1.close()
# user = data.split('\n')
# print(user)

#写文件
content = '故事很安静\n哈哈哈'
f2 = open('db', 'w')
f2.write(content)
f2.close()
