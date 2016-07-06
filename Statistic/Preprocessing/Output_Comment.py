#coding:utf-8

import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import  numpy as np

# data = np.load("data_new.npy")
# target = np.load("target_new.npy")

target = np.load("targetS.npy")

# m = 0
# data = list(data)
# target_oversampling = list(target)
# print len(target)
# for i in target:
#     if i == 1:
#         for t in range(1,31):   #重复40次
#             data.append(data[m])
#             target_oversampling.append(1)
#     m +=1
#
# print len(data)
# print len(target_oversampling)
#
# np.save('data_oversampling.npy',data)
# np.save('target_oversampling.npy',target_oversampling)
#
#
#
#



unironic = 0
ironic = 0
dontKnow = 0
con = sqlite3.connect("Feature.db")     #与数据库连接
cu = con.cursor()      #建立游标对象

for i in target:
   if i[1] == -1:
       unironic += 1
       cu.execute("select comment_content from Comment where comment_id = ? " , [i[0]])
       r = cu.fetchall()
       print r
   if i[1] == 0:
        dontKnow += 1
   if i[1] == 1:
        ironic += 1




print unironic
print dontKnow
print ironic
