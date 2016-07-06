#coding:utf-8

#建立原始特征集数据库
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#使用更加丰富的编码

#创建表

con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象
cu.execute("create table feature "
          "("
           "sentence_id integer not null,"
           "comment_id  integer not null,"
           "target integer not null,"
           "subreddit text not null,"
           "comment_sentence not null,"
           "thread TEXT not null)")   #text ID 7个属性,暂未加情绪, Thread是针对comment而言的


conR = sqlite3.connect("ironate.db")    #与原数据库连接
cuR = conR.cursor()
cuR.execute("select  irony_commentsegment.id ,irony_comment.id ,  label , subreddit , text , thread_title"
            " from  irony_commentsegment,irony_comment,irony_label "
            "where   irony_commentsegment.comment_id= irony_comment.id and  ( subreddit = 'Conservative' or subreddit = 'progressive' )  and irony_label.segment_id =irony_commentsegment.id"
            " order by  irony_commentsegment.id")

r = cuR.fetchall()

for result in r:
    print result[0]
    cu.execute("INSERT into feature VALUES (?,?,?,?,?,?)" , result)
con.commit()

con.close()
cuR.close()