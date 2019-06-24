#!/usr/bin/python
#  -*- coding:utf-8 -*-
# 四、购物车
# 功能要求：
# 要求用户输入总资产，例如：2000
# 1.显示商品列表，让用户根据序号选择商品，加入购物车
# 2.购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 3.附加：可充值、某商品移除购物车

# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
#
# balance = int(input('请输入资产:'))
# for i in range(0,len(goods)):
#     print('%s:%s:￥%s' %(i, goods[i]['name'], goods[i]['price']))
# choice = int(input('购买商品序号:'))
# if balance >= goods[choice]['price']:
#     balance -=  goods[choice]['price']
#     print('已成功购买%s, 余额:%s' %(goods[choice]['name'], balance))
# else:
#     print('余额不足')

#附加：可充值、某商品移除购物车
#1.输入余额之后打印所有功能: 1.购买商品 2.充值余额 3.移除商品
#2.把购物车的商品加入一个字典里
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998}
# ]
# shopping_car = [
# ]
#
# balance = int(input('请输入资产:'))
# while True:
#     choice = int(input('1.购买商品 2.充值 3.购物车管理 4.退出'))
#     #购买商品
#     if choice == 1:
#         while True:
#             print('-' * 20)
#             for i in range(0, len(goods)):
#                 print('%s:%s:￥%s' % (i, goods[i]['name'], goods[i]['price']))
#             print('-' * 20)
#             choice_goods = input('购买商品序号(b退出):')
#             if choice_goods == 'b':
#                 break
#             choice_goods = int(choice_goods)
#             if balance >= goods[choice_goods]['price']:
#                 balance -=  goods[choice_goods]['price']
#                 shopping_car.append(goods[choice_goods])
#                 print('商品 %s 已加入购物车, 余额:%s' %(goods[choice_goods]['name'], balance))
#             else:
#                 print('余额不足')
#     #充值
#     elif choice == 2:
#         print('当前余额:%s' %balance)
#         add_balance = input('请输入要充值的金额(b退出):')
#         if add_balance == 'b':
#             break
#         add_balance = int(add_balance)
#         balance += add_balance
#         print('充值成功,当前余额￥%s' %balance)
#     #购物车管理
#     elif choice == 3:
#         while True:
#             print('-------------当前购物车-----------------')
#             count = 0
#             for i in range(0, len(shopping_car)):
#                 print('%s  name:%s  price:￥%s ' %(i, shopping_car[i]['name'], shopping_car[i]['price']))
#                 count += shopping_car[i]['price']
#             print('-' * 20)
#             print('共消费:￥%s' %count)
#             manager_id = input('移除商品编号(b返回):')
#             if manager_id == 'b':
#                 break
#             manager_id = int(manager_id)
#             balance += shopping_car[manager_id]['price']
#             shopping_car.pop(manager_id)
#     #退出
#     elif choice == 4:
#         exit('bye,bye')