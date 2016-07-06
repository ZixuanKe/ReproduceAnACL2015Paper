#coding:utf-8

# ********************
# 整合特征并放入data之中
# ********************

#算法：
#上SGDClassfy 尝试是否可以改变Score
#Pipeline
#fit
#TrainTestSpilt + CrossValid
#x_train , x_target
#reshape


#评价：
#metrics.classification_report

#reproducer.data
#reproducer.targer
#考虑保存在pickle之中


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码

from sklearn import datasets #读入sklearn自带的数据集
from sklearn import svm      #导入SVM模型，测试UserGuide用
from sklearn.externals import joblib #用于永久保存模型到磁盘上
from sklearn.grid_search import GridSearchCV    #引入GridSearch模块
from sklearn.linear_model import LogisticRegression,SGDClassifier
import  numpy as np



tfidf_comment = list(np.load("tfidf_comment.npy"))
tfidf_thread = list(np.load("tfidf_thread.npy"))
bow =list(np.load("bow.npy"))
nnp = list(np.load("nnp.npy"))
subreddit = list(np.load("subreddit.npy"))
nnpp = list(np.load("nnpplus.npy"))
sentiment = list(np.load("sentiment.npy"))

data = tfidf_comment
#print tfidf
#print bow
#print nnp
#print subreddit
# data = nnp


for i in range(len(data)):
    print len(data[i])
    # for m in bow[i]:
    #    # print type(bow[i])
    #     data[i].append(m)
    for m in nnp[i]:
        data[i].append(m)
    for m in subreddit:
        data[i].append(m)
    for m in sentiment:
        data[i].append(m)
    for m in nnpp[i]:
        data[i].append(m)
    for m in tfidf_thread[i]:
        data[i].append(m)
    print len(data[i])

max = 0

for i in data:
    if len(i) > max:
        max = len(i)



print max

id = 1
for i in data:
    while len(i) < max:
         i.append(float(0))
    i.append(float(id))
    id += 1

np.save('data_new.npy',data)

list = list(np.load('target.npy'))

print 'target'
target = []
for i in list:
    target.append(float(i[0]))
print target


np.save('target_new.npy',target)
