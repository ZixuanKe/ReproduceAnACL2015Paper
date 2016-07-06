#coding:utf-8

import xlrd
from nltk.corpus import stopwords
import nltk
import numpy as np
from matplotlib import pyplot as plt

data = xlrd.open_workbook("Irony_Thread.xlsx")
table = data.sheets()[0]

nrows = table.nrows

row = ""
for i in range(1,nrows):
    row += str(table.row_values(i))


#1、分词(小写 停用词)
# 未用词干法
text = str(row).lower()
text = nltk.word_tokenize(text)


punctuation = ["u'i",',' , 'u', '``',"''" ,'.' , ":" ,";" ,'?' ,'(',')','[',']','&','!','*','@', '#','$','%' , '\\' , "'" ,'''"''','-','--',"'s","..."]

#字典形式记录单词出现次数
english_stopwords = stopwords.words('english')
hist = {}
for i in range(0,len(text)):
    if text[i] in punctuation or text[i] in english_stopwords:
        continue
    # if text[i+1]  in punctuation or [i+1] in english_stopwords:
    #     continue
    # if text[i+2]  in punctuation or [i+2] in english_stopwords:
    #     continue
    # trigram = str(text[i]) + " " + str(text[i+1]) + " " + str(text[i+2])
    # bigram = str(text[i]) + " " + str(text[i+1])
    # hist[bigram] = hist.get(bigram,0) + 1
    # hist[trigram] = hist.get(trigram,0) + 1
    hist[text[i]] = hist.get(text[i],0) + 1

hist = sorted(hist.iteritems(),key = lambda d:d[1] , reverse = True)

print len(text)
#图表形式输出
X = np.arange(0,20)
Y = []
xTicks = []
for i in range(0,20):
    Y.append(hist[i][1])
    xTicks.append(hist[i][0])

plt.bar(X,Y,facecolor='#9999ff', edgecolor='white')
plt.xticks(X,xTicks,rotation=90)
plt.title("Analyze Phrase Unigram")

plt.show()

