#!/usr/bin/env python
# coding=utf-8

"""
Python 函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。


"""

def printme( str ):
   # 打印传入的字符串到标准显示设备上
   print str
   return

# 调用函数
var1 = printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
print var1

"""
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""
# python 传不可变对象实例
def ChangeInt(a):
    a = 10
    return a

b = 2
var1 = ChangeInt(b)
print b  # 结果是 2
print var1

# 传可变对象实例
# 可写函数说明
def changeme(mylist):
    # 修改传入的列表
    mylist.append([1, 2, 3, 4])
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print "函数外取值: ", mylist


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return


# 调用printinfo函数
printinfo(age=50, name="miki")


def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name
    print "Age ", age
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(name="miki")


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)