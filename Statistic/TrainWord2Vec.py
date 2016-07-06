#coding:utf-8

from gensim.models import Word2Vec
from nltk.corpus import stopwords
import nltk
import xlrd

punctuation = ["u'it\\u2019s","u'i",',' , 'u', '``',"''" ,'.' , ":" ,";" ,'?' ,'(',')','[',']','&','!','*','@', '#','$','%' , '\\' , "'" ,'''"''','-','--']

#字典形式记录单词出现次数
english_stopwords = stopwords.words('english')


data = xlrd.open_workbook("UnIrony_Comment_PT.xlsx")
table = data.sheets()[0]

nrows = table.nrows

sentence = []
for i in range(nrows):
    row = str(table.row_values(i))
    text = str(row).lower()
    text = nltk.word_tokenize(text)
    sentence.append(text)
model = Word2Vec(sentence, min_count=1)
model.save("Comment_UnIrony_In_PT.word2vec")