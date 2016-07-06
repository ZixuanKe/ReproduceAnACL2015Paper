#coding:utf-8

#3、NNP+特征
import nltk
import  re
from sklearn.feature_extraction.text import CountVectorizer
import sqlite3
#引入sklearn里的计数向量
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码

con = sqlite3.connect("Feature_Progressive_Conservative.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

# cu.execute("create table NNPPLUS_feature "
#            "("
#         "Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),"
#            "NNPPLUS TEXT not null"
#            ")")

cu.execute("select DISTINCT comment_id,thread from feature ORDER BY rowid")   #查询语句

r = cu.fetchall()


bowvectorizer =  CountVectorizer(min_df = 1 , stop_words = 'english')

list = []


for comment_sentence in r:

        result = str(comment_sentence[1]).replace("[","").replace("]","").replace('''"''',"")

        words = nltk.word_tokenize(result)
        result = ""
        pos = nltk.pos_tag(words)
        for word in pos:
            if word[1] == "NNP":
                    result += word[0]
        list.append(result)

bownnpp = bowvectorizer.fit_transform(list)
bowArray = bownnpp.toarray()
bowArray.save("temp.npy")

for nnpp in range(len(bowArray)):
        print r[nnpp][0]
        print bowArray[nnpp]
        list = [int(r[nnpp][0]),str(bowArray[nnpp])]
        cu.execute("INSERT INTO NNPPLUS_feature VALUES (?,?)",list)
con.commit()

con.close()