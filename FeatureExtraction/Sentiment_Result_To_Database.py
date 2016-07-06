#coding:utf-8

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象


#新建一个sentiment表 放入表中
#重新保存为npy
#再合并计算观察最终结果
#cu.execute('CREATE TABLE Sentiment_feature (Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),sentiment integer not null)')


cu.execute("select  DISTINCT Comment_id from Comment ")   #查询语句

r = cu.fetchall()
file = open('result.txt')
try:
     all_the_text = file.read( )
finally:
     file.close( )

count = 0
for i in all_the_text:
    if i == '\n':
        continue
    count += 1
    print count
    #print id


    #list = [int(id[0]) , int(all_the_text[count])]
    #count += 1
    #cu.execute('INSERT into Sentiment_feature VALUES (?,?)',list)
#con.commit()
