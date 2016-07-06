#coding:utf-8

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

cu.execute("select DISTINCT thread from feature where target = 1 ORDER BY rowid")   #查询语句

r = cu.fetchall()
print len(r)
file = open("IronyText_Origin_Thread.txt","w")
for thread in r:
    file.write(str(thread[0] +  "." + "\n"))

file.close()

cu.execute("select DISTINCT thread from feature where target = -1 ORDER BY rowid")   #查询语句

r = cu.fetchall()

file = open("UnIronyText_Origin_Thread.txt","w")
for thread in r:
    file.write(str(thread[0] + "." + "\n"))
file.close()