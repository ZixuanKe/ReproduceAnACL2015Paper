#coding:utf-8

#3、BOW特征
from sklearn.feature_extraction.text import TfidfVectorizer
import sqlite3
#引入sklearn里的计数向量
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码

con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

# cu.execute("create table TFIDF_Thread_feature "
#            "("
#           "Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),"
#            "TFIDF TEXT not null"
#            ")")

cu.execute("select DISTINCT comment_id,thread from feature ORDER BY rowid")   #查询语句

r = cu.fetchall()


tfidfvectorizer =  TfidfVectorizer(min_df = 1 , stop_words = 'english')

i = 0
id = []
list = []

for comment_sentence in r:

    print id


    if i == 0:
        list.append(comment_sentence[1])
        id.append(comment_sentence[0])
        i = i+1
    elif comment_sentence[0] != id[len(id)-1]:
        Idresult = id[len(id)-1]
        id = []
        id.append(comment_sentence[0])
        result = list
        list = []
        print result
        list.append(comment_sentence[1])
        #对result 计算TFIDF的值
        try:
            tfidf = tfidfvectorizer.fit_transform(result)
            array = tfidf.toarray()
        except Exception:
            print 'Exception'
            for x in result:
                x = 0
            array = result          #只有停用词的帖子，词袋清0
        print array
        m = [Idresult,str(array)]
        cu.execute("INSERT INTO TFIDF_Thread_feature VALUES (?,?)",m)
        con.commit()

    else:
        list.append(comment_sentence[1])
        id.append(comment_sentence[0])


Idresult = id[len(id)-1]
result = list
print result
#对result 计算TFIDF的值
try:
    tfidf = tfidfvectorizer.fit_transform(result)
    array = tfidf.toarray()
except Exception:
    print 'Exception'
    for x in result:
        x = 0
        array = result          #只有停用词的帖子，词袋清0
print array
m = [Idresult,str(array)]
cu.execute("INSERT INTO TFIDF_Thread_feature VALUES (?,?)",m)
con.commit()

con.close()