#!/usr/bin/python
# -*- coding:utf-8 -*-

################### dict: 字典#########
dic  = {
    'k1':'v1',
    'k2':'v2',
    'k3':'v3'
}

# 1.清空
# dic.clear()
# print(dic)

# 2. 浅拷贝
# v = dic.copy()
# print(v)

# 3. 根据key获取value值
# v1 = dic.get('k1', 11) #不存在不报错，不存在返回11
# v2 = dic['k1']
# print(v1 , v2)

# 4. 删除并获取对应value值
# v = dic.pop('k1')
# del dic['k1']
# print(v)

# 5.随机删除键值对，并获取key 和value
# k,v = dic.popitem()
# print(dic)

# 6.不存在时新增，已存在不操作 setdefault
# dic.setdefault('k4', 'v4')
# print(dic)

# 7. （批量处理）不存在时新增,已存在就更新
# dic.update({'k3':'111', 'k4':'v4'})
# print(dic)

#8. 指定value值创建新字典
# dic_ = dict.fromkeys(['k1', 'k2', 'k3'], [11,22])
# print(dic_)


###########  # 额外 ############
# -字典可以嵌套
# - 字典key必须是不可变类型（元组，字符串等,bool,数字）
# dic  ={
#     'k1':'v1',
#     'k2':[1, 2, 3,],
#     True:'ff', #True  为1
#     0:'aa',  # 0 为False
#     1:'222',
# }