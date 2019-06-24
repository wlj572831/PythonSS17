#!/usr/bin/python
# -*- coding:utf-8 -*-

# ################# list 列表 ###########
# user_list = ['张三', '李四', '王五']

# 1. 追加 append()
# user_list.append('李铭')
# print(user_list)

# 2. 清空 clear()
# user_list.clear()
# print(user_list)

# 3. 拷贝（浅拷贝）
# v = user_list.copy()
# print(v)

# 4. 获取元素个数
# v = user_list.count('张三')
# print(v)

# 5.扩展，遍历参数里的内容，扩展到列表里
# user_list.extend(['盖伦', '拉克丝'])
# print(user_list)

# user_list = ['张三', '李四', '王五']
# 6. 查找元素的索引，没有报错
# v = user_list.index('张三')
# print(v)

# 7. 删除并获取元素 pop(@a)
# @a 表示索引位置，为空就默认最后一个元素
# v = user_list.pop(1)
# print(v, user_list)

# 8. 根据值进行删除
# user_list.remove('张三')
# print(user_list)

# 9. 列表顺序翻转 reverse()
# user_list.reverse()
# print(user_list)

num_list = [1, 21, 50, 15, 12]

# 10. 从小到大排序， sort([reverse=False])
# True 从大到小
# num_list.sort()
# print(num_list)

########### 额外 ###########
# user_list[0]
# user_list[1:3]
# user_list[0:3:1]
# del user_list[2]
# for i in user_list:
#     print(i)