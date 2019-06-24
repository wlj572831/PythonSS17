#!/usr/bin/python
# -*- coding:utf-8 -*-

# ################ set 集合:不可重复的列表###################

se = {'alex', 'error', 'cc'}
se2 = {'alex', 'wang', 'bb'}
se3 = {'alex', }

# 1.添加 add
# se.add()

# 2.清除 clear
# se.clear()

# 3. se相对se2的单向差集(se存在，se2不存在)
# v = se.difference(se2)
# print(v)

# 4. 差集
# v = se.symmetric_difference(se2)
# print(v)

# 5. 交集
# v = se.intersection(se2)
# print(v)

# 6. 并集
# v = se.union(se2)
# print(v)

#  7. 把获取到的集合重新扶赋值给se
# se.difference_update(se2)
# se.intersection_update(se2)
# se.symmetric_difference_update(se2)

# 8. 移除指定值
# se.discard('alex')
# print(se)

# 9. 是否有交集,有False 无True
# v = se.isdisjoint(se)
# print(v)

# 10. 是否是子集
# v = se.issubset(se3)
# print(v)

# 11.是否是父集
# v = se.issuperset(se3)
# print(v)

# 12. 其他
# se .pop() #删除并返回值
# se.remove() #删除
# se.update() #批量更新

# 13.
#没有索引，能for 循环
#可嵌套元组、不可嵌套字典和列表