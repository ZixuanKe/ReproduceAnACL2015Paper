#coding:utf-8

#打印所有comment
import sqlite3
#引入sklearn里的计数向量
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码

con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

cu.execute("select DISTINCT comment_content from Comment ORDER BY rowid")   #查询语句

r = cu.fetchall()

sample_list = []

for i in r:
    sample_list.append( str(i).replace("]","").replace("[","").replace("(u\'","").replace('(u"',"").replace("\'",""))

file  = open("sentiment.txt",'w')
for line in sample_list:
    sample_list = [str(line) + '\n' ]
    file.writelines(sample_list)
file.close()
