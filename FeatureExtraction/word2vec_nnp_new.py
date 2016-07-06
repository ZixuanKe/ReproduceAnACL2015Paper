#coding:utf-8

from gensim.models import Word2Vec
from nltk.corpus import stopwords
import nltk
import sqlite3
#matplotlib inline


con = sqlite3.connect("Feature_Progressive_Conservative.db")     #与数据库连接
cu = con.cursor()      #建立游标对象
cu.execute("create table word2vec_NNP_new_feature "
          "("
         "Comment_id  integer not null  PRIMARY KEY REFERENCES feature(Comment_id),"
          "word2vec_NNP TEXT not null"
          ")")


cu.execute("select NNP from NNP_feature ")
r = cu.fetchall()

nnp = []
for i in r:
    temp = (i[0].replace('[','').replace(']','').replace('\n','').replace(",",""))
    temp = temp.split(' ')
    list = []
    for m in temp:
        list.append(float(m))
    nnp.append(list)

cu.execute("select comment_id,word2vec_nnp from word2vec_nnp_feature ")
r = cu.fetchall()


score = []
for i in r:
    temp = (i[1].replace('[','').replace(']','').replace('\n','').replace(",",""))
    temp = temp.split(' ')
    list = []
    for m in temp:
        try:
            list.append(float(m))
        except Exception:
            #print Exception
            list.append(float(0))
    score.append(list)

ks = []
for i in score:
    for s in i:
        if s != 0:
            ks.append(s)

print ks

count = 0
for ind in range(len(nnp)):

    for nnp_r in range(len(nnp[ind])):
        if nnp[ind][nnp_r] == 1:
           print "Yes"
           print count
           print len(score[ind])
           nnp[ind][nnp_r] = ks[count]
           count+=1

    result = [r[ind][0],str(nnp[ind])]
    cu.execute("INSERT INTO word2vec_NNP_new_feature VALUES (?,?)",result)
con.commit()
