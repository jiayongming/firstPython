#!/usr/bin/env python
# coding=utf-8
from filecmp import cmp

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list1.append("111")
print("list1[0]: ", list1[4])

del list1[0]
print("list1[0]: ", list1[0])
print(len(list1))

print(cmp(list1 , list2))
print(max(list1))
