#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pymysql


class DB():
    def __init__(self, host='localhost', port=3306, db='wine', user='analyse', passwd='GemanticYes!', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with DB(host='10.0.0.246', user='analyse', passwd='GemanticYes!', db='wine') as db:
        result = db.execute('select * from pay_record')
        print(result)
        print(db)
        for i in db:
            print(i)

"""
with…as语句执行顺序：
–>首先执行expression里面的__enter__函数，它的返回值会赋给as后面的variable，想让它返回什么就返回什么，只要你知道怎么处理就可以了，如果不写as variable，返回值会被忽略。
–>然后，开始执行with-block中的语句，不论成功失败(比如发生异常、错误，设置sys.exit())，在with-block执行完成后，会执行expression中的__exit__函数。

当with...as语句中with-block被执行或者终止后，这个类对象应该做什么。如果这个码块执行成功，则exception_type,exception_val, trace的输入值都是null。
如果码块出错了，就会变成像try/except/finally语句一样，exception_type, exception_val, trace 这三个值系统会分配值。
"""
