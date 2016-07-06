#coding:utf-8

#3、BOW特征
from sklearn.feature_extraction.text import CountVectorizer
import sqlite3
#引入sklearn里的计数向量
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码

con = sqlite3.connect("Feature_Progressive_Conservative.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

# cu.execute("create table BOW_feature "
#            "("
#           "Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),"
#            "BOW TEXT not null"
#            ")")

cu.execute("select DISTINCT comment_id,comment_content from comment ORDER BY rowid")   #查询语句

r = cu.fetchall()



bowvectorizer =  CountVectorizer(min_df = 1 , stop_words = 'english')

list = []
for comment_sentence in r:
    result = str(comment_sentence[1]).replace("[","").replace("]","").replace('''"''',"")
    list.append(result)
    bow = bowvectorizer.fit_transform(list)
print bow.shape

# for feature in range(1301):
    # list = []
    # list = [r[feature][0],bow[feature]]
#     cu.execute("INSERT INTO BOW_feature VALUES (?,?)",list)
# con.commit()
#
# con.close()