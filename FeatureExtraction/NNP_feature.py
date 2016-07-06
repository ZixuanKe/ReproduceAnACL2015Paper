#coding:utf-8

#3、NNP+特征
import nltk
import  numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import sqlite3
#引入sklearn里的计数向量
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码

con = sqlite3.connect("Feature_Progressive_Conservative.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

# cu.execute("create table NNP_feature "
#            "("
#         "Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),"
#            "NNP TEXT not null"
#            ")")

cu.execute("select DISTINCT comment_id,comment_content from comment ORDER BY rowid")   #查询语句

r = cu.fetchall()

#
# bowvectorizer =  CountVectorizer(min_df = 1 , stop_words = 'english')
#
# list = []
#
#
# for comment_sentence in r:
#
#         result = str(comment_sentence[1]).replace("[","").replace("]","").replace('''"''',"")
#
#         words = nltk.word_tokenize(result)
#         result = ""
#         pos = nltk.pos_tag(words)
#         for word in pos:
#             if word[1] == "NNP":
#                     result += word[0] + " "
#         list.append(result)
#
# bownnpp = bowvectorizer.fit_transform(list)

bowArray = np.load("array.npy")
print bowArray.shape

m = []
for nnpp in range(len(bowArray)):
        result = list(bowArray[nnpp])
        m = [int(r[nnpp][0]),str(result)]
        cu.execute("INSERT INTO NNP_feature VALUES (?,?)",m)
con.commit()

con.close()
