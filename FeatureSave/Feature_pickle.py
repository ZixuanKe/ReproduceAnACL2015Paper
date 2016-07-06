##coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码
import sqlite3
import numpy as np
con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

#target
cu.execute("select comment_id , target from feature ")
r = cu.fetchall()

id = 3
targetTemp = 0
target = []
count = 1
ironic = False
for m in r:

    if m[0] == id:

        if count <= 3:

            targetTemp = targetTemp +m[1]
            count = count + 1
            id = m[0]

        else:
            if targetTemp > 0:
                ironic = True
                targetTemp = m[1]
                count = 2
                id = m[0]
            else :
                targetTemp = m[1]
                count = 2
                id = m[0]
    else:

        if ironic == True:

            list = [m[0],1]
            target.append(list)
            targetTemp = m[1]
            id = m[0]
            ironic = False
            count = 2
        else:

            list = [m[0],-1]
            target.append(list)
            targetTemp =  m[1]
            id = m[0]
            ironic = False
            count = 2
#原则：
#1、sentence内部少数服从多大数(相加为1/-1)
#2、comment内至少有一个句子为ironic
if ironic == True:

            list = [m[0],1]
            target.append(list)

else:
            list = [m[0],-1]
            target.append(list)


#原则：

print len(target)
target = np.array(target)
target = target.reshape(len(target),2)

# np.save('targetS.npy',target)
print target


#TFIDF_Comment
cu.execute("select TFIDF from TFIDF_feature ")
r = cu.fetchall()
tfidf = []
c = 0
for i in r:
    temp = (i[0].replace('[','').replace(']','').replace('\n',''))
    temp = temp.split(' ')
    list = []
    for m in temp:
        try:
            list.append(float(m))
        except Exception:
            #print Exception
            list.append(float(0))
    tfidf.append(list)

tfidf = np.array(tfidf)

print len(tfidf)
print tfidf
#np.save('tfidf.npy',tfidf)

#TFIDF_Thread
cu.execute("select TFIDF from TFIDF_Thread_feature ")
r = cu.fetchall()
tfidf = []
c = 0
for i in r:
    temp = (i[0].replace('[','').replace(']','').replace('\n',''))
    temp = temp.split(' ')
    list = []
    for m in temp:
        try:
            list.append(float(m))
        except Exception:
            #print Exception
            list.append(float(0))
    tfidf.append(list)

tfidf = np.array(tfidf)

print len(tfidf)
print tfidf
np.save('tfidf_thread.npy',tfidf)




#BOW
cu.execute("select BOW from BOW_feature ")
r = cu.fetchall()

bow = []
c = 0
for i in r:

    temp = (i[0].replace('[','').replace(']','').replace('\n',''))
    temp = temp.split(' ')
    list = []
    for m in temp:
        try:
            list.append(float(m))
        except Exception:
            #print Exception
            list.append(float(0))
    bow.append(list)

bow = np.array(bow)

print len(bow)
print bow
print bow.dtype
#np.save('bow.npy',bow)

#NNP
cu.execute("select NNP from NNP_feature ")
r = cu.fetchall()
nnp = []
c = 0
for i in r:
    temp = (i[0].replace('[','').replace(']','').replace('\n',''))
    temp = temp.split(' ')
    list = []
    for m in temp:
        try:
            list.append(float(m))
        except Exception:
            #print Exception
            list.append(float(0))
    nnp.append(list)

nnp = np.array(nnp)
print len(nnp)
print nnp
# np.save('nnp.npy',nnp)


#subreddit
cu.execute("select subreddit from Subreddit_feature ")
r = cu.fetchall()

subreddit = np.array(r)

print len(subreddit)
print subreddit
#np.save('subreddit.npy',subreddit)

#NNP+
#NNP
cu.execute("select NNPPLUS from NNPPLUS_feature ")
r = cu.fetchall()
nnp = []
c = 0
for i in r:
    temp = (i[0].replace('[','').replace(']','').replace('\n',''))
    temp = temp.split(' ')
    list = []
    for m in temp:
        try:
            list.append(float(m))
        except Exception:
            #print Exception
            list.append(float(0))
    nnp.append(list)

nnp = np.array(nnp)
print len(nnp)
print nnp
# np.save('nnpplus.npy',nnp)





#sentiment
cu.execute("select sentiment from Sentiment_feature ")
r = cu.fetchall()

sentiment = np.array(r)

print len(sentiment)
#print sentiment
#np.save('sentiment.npy',sentiment)