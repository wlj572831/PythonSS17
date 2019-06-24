#!/usr/bin/python
#  -*- coding:utf-8 -*-

#一、元素分类
#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，
# 将小于 66 的值保存至第二个key的值中。即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# num_list = [11,22,33,44,55,66,77,88,99,90,100]
# num_dict = {'k1':[], 'k2':[]}
# for i in  num_list:
#     if i > 66:
#         num_dict['k1'].append(i)
#     else:
#         num_dict['k2'].append(i)
# print(num_dict)

#二、查找
#查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
# li = ["alec ", " aric", "Alex", "Tony ", "rain "]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex ", 'k2': ' aric ',  "k3": "Alex ", "k4": "Tony "}
#
# for i in range(0,len(li)):
#     li[i] = li[i].strip()
# print(li)

#三、输出商品列表，用户输入序号，显示用户选中的商品
# li = ["手机", "电脑", '鼠标垫', '游艇']
# choice = int(input('请输入要选择的商品序号,%s:' %str(li)))
# print(li[choice])
