#!/usr/bin/python
# -*- coding:utf-8 -*-


#1.capitalize 首字母大写
# name = 'alex'
# v = name.capitalize()
# print(v)

#2.casefold 所有大写变小写
# name = 'ALEX'
# v1 = name.casefold()

#3. lower所有大写变小写
# v2 = name.lower()
# print(v1, v2)

#4.center(a,b)
# a表示总长度
# b表示填充的内容(选填)
# name = 'alex'
# v = name.center(20, '*')
# print(v)

#5. count(a, [start], [end])
# 参数1: 要查找的值(子序列)
# 参数2：起始位置(索引)
# 参数3：结束位置(索引)
# name = 'aleaa'
# v = name.count('a')
# print(v)

# name = 'alex'

# 6. endswith(a) 是否以a结尾
# v = name.endswith('ex')
# print(v)

#7.startswith(a) 是否以a开始
# v1 = name.startswith('al')
# print(v1)

#8.转换成字节 encode
# name = '李杰'
# v = name.encode(encoding='utf-8')
# print(v)
#
# v1 = name.encode(encoding='gbk')
# print(v1)

#9.找到制表符\t，进行替换
#PS：指定的长度包含\t前面的字符
# name = 'a\talex'
# v = name.expandtabs(20)
# print(v)

#10. find(a, [start], [end])
# 找到指定值在对象中的索引, 没有返回-1
# @start @end表示开始结束范围
# name = 'alex'
# v = name.find('al')
# print(v)

#11. 字符串格式化
#format根据索引传值
# tpl = "我是:{0}; 年龄:{1}, 性别:{2}"
# v1 = tpl.format('李杰', 18, '男')
# print(v1)
#format根据值传值
# tpl = "我是:{name}; 年龄:{age}, 性别:{sex}"
# v1 = tpl.format(name='李杰', age=18, sex='男')
# print(v1)

# format_map 传入字典整体
# tpl = "我是:{name}; 年龄:{age}, 性别:{sex}"
# v1 = tpl.format_map({'name':'lijie', 'age':18, 'sex':'' })
# print(v1)

# 12. 是否是数字、汉字
# name = 'alex8汉字'
# v1 = name.isalnum() #字,数字
# print(v1) #True
# v2 = name.isalpha() #
# print(v2) #False

# 13 .判断是否是数字
# num = '②'
# v1 = num.isdecimal() # '123'
# v2 = num.isdigit() # '123' '②'
# v3 = num.isnumeric() #'123', '二', '②'
# print(v1,v2,v3)

# 14.是否是标识符
# n = 'name'
# v = n.isidentifier()
# print(v) #True

#15.大小写转换和判断
# islower 是否全部小写
# isupper 是否全部大写
# name = 'alex'
# v = name.islower()
# print(v)
# v1 = name.isupper()
# print(v1)
# upper 全部变大写
# lower 全部变小写
# v = name.upper()
# v1 = name.lower()
# print(v, v1)

#16.是否全部是空格 isspace()
# name = ' '
# v = name.isspace()
# print(v)

#17.元素拼接 a.join(b)
# 用a将b内所有字符隔开
# name = 'alex'
# v = name.join('--')
# v1 = '-'.join(name)
# print(v, v1)

#18. 左右填充
# name = 'alex'
# v = name.rjust(20, '*')
# print(v)
#
# v1 = name.ljust(20, '*')
# print(v1)

#19. 对应关系 + 翻译
# m = str.maketrans('alex', '1234') #一一对应
# name = 'abblfasfeaffx'
# v = name.translate(m)
# print(v)

#20. 分割，保留分割的元素
# content = '李泉烧饼刘康'
# v = content.partition('烧饼') #rpartition 从右开始分割
# print(v)

#21. 替换
# @count替换的个数
# content = 'right**error'
# v = content.replace('**', 'and'，@count)
# print(v)

#22. 字符串分割
# name ='a_l_e_x'
# v = name.split('_')
# print(v)

#23 .strip() 移除空白 \n \t或字符
# name = 'alex'
# v =  name.strip('a')
# print(v)

#24. 大小写转换
# name = 'Alex'
# # v = name.swapcase()
# # print(v)

##### 字符串功能总结:
# #常用方法
# name = 'alex'
# name.upper()
# name.lower()
# name.split()
# name.find()
# name.strip()
# 'alex'.join(['a', 'b'])
# name.startswith()
# name.format()
# name.replace()
# # 额外功能
# name[0]
# name[0:3]
# name[0:3:2]
# len(name)
# for i in name