#!/usr/bin/env python
# coding=utf-8

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print(("dict['Name']: ", dict['Name']))
print(("dict['Age']: ", dict['Age']))

dict['Age'] = 8 # 更新
dict['School'] = "RUNOOB" # 添加
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name']  # 删除键是'Name'的条目
dict.clear()  # 清空字典所有条目
del dict  # 删除字典

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])