#!/usr/bin/env python
# coding=utf-8

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()


try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print("Error: 没有找到文件或读取文件失败")

# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as a:
        print("参数没有包含数字\n", a)

# 调用函数
temp_convert("xyz")