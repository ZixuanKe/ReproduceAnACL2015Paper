#coding:utf-8

from gensim.models import Word2Vec
import xlrd
from nltk.corpus import stopwords
import nltk
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
import xlrd
#matplotlib inline


model = Word2Vec.load("Comment_Irony_In_AC.word2vec")
punctuation = ["u'it\\u2019s","u'i",',' , 'u', '``',"''" ,'.' , ":" ,";" ,'?' ,'(',')','[',']','&','!','*','@', '#','$','%' , '\\' , "'" ,'''"''','-','--']

#字典形式记录单词出现次数
english_stopwords = stopwords.words('english')


data = xlrd.open_workbook("Irony_Comment_AC.xlsx")
table = data.sheets()[0]



nrows = table.nrows

for i in range(nrows):
    count = 0
    row = str(table.row_values(i))
    text = str(row).lower()
    text = nltk.word_tokenize(text)
    for word in text:
        if word in punctuation or word in english_stopwords:
            continue
        tempSimilar = model.most_similar(word)
        for similarWord in tempSimilar:
            if similarWord[0] in text:
                count += 1
    print count


