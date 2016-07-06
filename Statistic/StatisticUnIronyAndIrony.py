#coding:utf-8
import nltk
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
totalIrony = len(text)


punctuation = ["u'i",',' , 'u', '``',"''" ,'.' , ":" ,";" ,'?' ,'(',')','[',']','&','!','*','@', '#','$','%' , '\\' , "'" ,'''"''','-','--',"'s","..."]

#字典形式记录单词出现次数
english_stopwords = stopwords.words('english')
hist_Irony = {}
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
    hist_Irony[text[i]] = hist_Irony.get(text[i],0) + 1

hist_Irony = sorted(hist_Irony.iteritems(),key = lambda d:d[1] , reverse = True)

# print hist_Irony

hist_Top20IronyInUnitony = {}

file = open("UnIronyText_Origin_Thread.txt")
try:
    allTheText = file.readlines()
finally:
    file.close()

word_Unirony = []
for line in allTheText:
      text = line.lower()
      word_Unirony.append(nltk.word_tokenize(text))

totalUnirony = 0
for word_Irony in hist_Irony:
    gram = word_Irony[0]
    hist_Top20IronyInUnitony[gram] = hist_Top20IronyInUnitony.get(gram,0)
    for single_Word_Unirony in word_Unirony:
        for Single_Word_Uniron in single_Word_Unirony:
            totalUnirony += 1
            if gram == Single_Word_Uniron:
                hist_Top20IronyInUnitony[gram] = hist_Top20IronyInUnitony.get(gram,0) + 1


print hist_Top20IronyInUnitony


y = np.arange(0,20)
x1 = []
x2 = []
yTicks = []
count = 1

for i in hist_Irony:
    x1.append(i[1])
    x2.append(hist_Top20IronyInUnitony[i[0]])
    yTicks.append(i[0])
    count += 1
    if count == 21:
        break

for i in range(len(x1)):
    #x1[i] = x1[i]/2590.0
    x1[i] = x1[i]/(1.0 * totalIrony)
for i in range(len(x2)):
    # x2[i] = x2[i]/(60528.0)
    print x2[i]
    x2[i] = x2[i]/(1.0 * totalUnirony)

print totalUnirony
print totalIrony

plt.yticks(y,yTicks)
plt.ylabel('Word')
plt.xlabel('Frequency(Total Occurrences/Total Words)')
plt.plot(x1,y,'--or',label = 'Irnoy')
plt.plot(x2,y,'-ob' , label = 'UnIrony')
plt.legend()
plt.show()