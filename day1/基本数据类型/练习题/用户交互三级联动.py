#!/usr/bin/python
#  -*- coding:utf-8 -*-

# 五、用户交互，显示省市县三级联动的选择
dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        ...
    },
    "山西": {
        ...
    }

}
# 1.打印第一级省份，选择要进入的省份b退出
# 2.进入第二级，选择要进入的第二级,b返回上级
# 3.打印最后一级 b返回上级

# 丐版
# for fi in dic:
#     print(fi)
# choice_1 = input('请输入要进入的省份:')
# #进入省份，显示第二级
# for city in dic[choice_1]:
#     print(city)
# choice_2 = input('请输入要进入的省市:')
# #进入第二级，显示第三级
# for country in dic[choice_1][choice_2]:
#     print(country)

# 假装很强版
# while True:
#     for fi in dic:
#         print(fi)
#     choice = input('请选择:')
#     if choice in dic:
#          dic = dic[choice]
#     else:
#         continue

#终极版本
#1.循环列表，显示第一级菜单
#2.记录第一级菜单到last_list，并进入下一级
#3.循环显示第二级菜单，如果选择b，则利用pop函数返回最后一次记录的状态重新赋给dic
# last_list = []
# while True:
#     for fi in dic:
#         print(fi)
#     choice = input('请选择:')
#     if choice in dic:
#         #记录进入下一级菜单之前的状态
#         last_list.append(dic)
#         dic = dic[choice]
#     elif choice == 'b':
#         #取出列表中上一级的内容
#         dic = last_list.pop()
#     else:
#         continue
