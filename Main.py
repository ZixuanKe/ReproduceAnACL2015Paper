
#coding:utf-8
from sklearn import datasets #读入sklearn自带的数据集
from sklearn import svm      #导入SVM模型，测试UserGuide用
from sklearn.externals import joblib #用于永久保存模型到磁盘上
from sklearn.grid_search import GridSearchCV    #引入GridSearch模块
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_recall_curve, roc_curve, auc
import sqlite3
import  numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#更改默认编码 使用更加丰富的编码


con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象


data = np.load("data_new.npy")
target = np.load("target_new.npy")

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = 0.2)
#应该是ironic 和 anironic 分别取样，以求平衡
#搞出多种anironic的重复 再进行抽样 （最简单的imbalanced处理）


average = 0
testNum = 500


#加入NNP+ 提升5%
#如何找出Bad Case???


for i in range(0, testNum):
    #加载数据集，切分数据集80%训练，20%测试
    while True:
        x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = 0.2)

        count = 0
        for test in y_test:
            if(test == 1):
                count += 1
        if count == 8 :
            break
    #采样：限定在-1中选择8个


    #训练LR分类器
    x_train = list(x_train)
    y_train = list(y_train)

    for over in range(len(y_train)):
        if y_train[over] == 1:
            for overSampling in range(0,0):    #设定过采样次数
                x_train.append(x_train[over])
                y_train.append(1)



    x_train = np.array(x_train)
    y_train = np.array(y_train)

    id = x_test[:,len(x_test[0])-1]

    x_test = x_test[:,0:len(x_test[0])-1]
    #去掉序号
    x_train = x_train[:,0:len(x_train[0])-1]

    dict = {"":""}
    for h in range(len(x_test)):
        dict[h] = id[h]
    #对训练集过采样

    clf = SGDClassifier(penalty = 'elasticnet' , loss = 'log') #elasticnet要好于默认LR
    # clf = svm.SVC(gamma = 0.001 , C = 100) #SVM整体表现要好于线性模型 Tsne证明?
    #clf = LogisticRegression()
    clf.fit(x_train, y_train)	#将训练集放入分类器之中
    print 'Report : '
    y_predicted = clf.predict( x_test )
    print classification_report(y_test,y_predicted)	#输出F1 和 Recall

    # print "Bad Cases: "
    # for result in range(len(y_test)):
    #     if y_test[result] != y_predicted[result] and y_test[result] == 1:
    #         listR = [dict[result]]
    #         cu.execute("select DISTINCT comment_content from Comment where rowid = ?" , listR)   #查询语句
    #         r = cu.fetchall()
    #
    #         for comment in r:
    #             print str(comment)


#准确率与召回率
