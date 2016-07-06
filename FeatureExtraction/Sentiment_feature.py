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



cu.execute("select DISTINCT comment_id,comment_sentence from feature ORDER BY rowid")   #查询语句

r = cu.fetchall()

#cu.execute("create table Comment "
 #          "("
  #        "Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),"
   #        "Comment_content text not null"
    #       ")")

i = 0
id = []
list = []
result = []
temp = []

for comment_sentence in r:

    if i == 0:
        list.append(str(comment_sentence[1]).replace('[','').replace(']','').replace('\n',''))
        id.append(comment_sentence[0])
        i = i+1
    elif comment_sentence[0] != id[len(id)-1]:
        tempId = id[0]
        id = []
        id.append(comment_sentence[0])
        result = list
        list = []
        list.append(str(comment_sentence[1]).replace('[','').replace(']','').replace('\n',''))
        temp = [tempId , str(result) ]
        #print result
       # cu.execute("INSERT INTO Comment VALUES (?,?)",temp)
       # con.commit()
    else:
        list.append(str(comment_sentence[1]).replace('[','').replace(']','').replace('\n',''))
        id.append(comment_sentence[0])



tempId = id[0]
id.append(comment_sentence[0])
result = list
temp = [tempId , str(result).replace('[','').replace(']','').replace('\n','').replace("\'&gt;","").replace("\'","") ]
print temp
cu.execute("INSERT INTO Comment VALUES (?,?)",temp)
con.commit()


con.close()