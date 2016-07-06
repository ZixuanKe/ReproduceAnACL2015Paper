#coding:utf-8

import sqlite3
#引入sklearn里的计数向量
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码

con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

#cu.execute("create table Subreddit_feature "
 #          "("
  #        "Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),"
   #        "subreddit integer not null"
    #       ")")

cu.execute("select  DISTINCT feature.comment_id, subreddit from feature,BOW_feature where feature.comment_id = BOW_feature.comment_id")   #查询语句

r = cu.fetchall()

for i in r:
    if i[1] == 'Conservative':
        insert = 1
    else:
        insert = 0
    list = [i[0],insert]
    cu.execute("INSERT into Subreddit_feature VALUES (?,?)",list)   #查询语句

con.commit()
con.close()
