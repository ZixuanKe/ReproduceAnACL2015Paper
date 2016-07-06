#coding:utf-8

#使用脚本去掉停用词等再找搭配
from nltk.corpus import stopwords
import nltk
import numpy as np
from matplotlib import pyplot as plt


# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
#

#
#
# file = open("IronyText.txt")
# allTheText = file.readlines()
#
# for line in allTheText:
#     line = str(line).lower()
#     text = nltk.word_tokenize(line)
#     for i in text:
#         if i in punctuation or i in english_stopwords:
#           line = line.replace(i,"")
#     print line
#   以上清理句子数据以查找词语匹配
#   清理之后词语搭配不再完整


#找到具有依存关系的词语搭配
import re

file = open('Result_Irony_Dependency_Thread.txt')

try:
    allTheText = file.readlines()
finally:
    file.close()

result_Irony = []
for line in allTheText:
    if line.find("nsubj")!= -1:
        line = line.replace("\n","").replace("nsubj","").replace("(","").replace(")","").replace("-","").replace(" ","")
        rule = re.compile("[0-9]")
        line = rule.sub("",line)

        result_Irony.append(line.split(","))

file.close()


hist_Irony = {}
english_stopwords = stopwords.words('english')
punctuation = ["u'i",',' , 'u', '``',"''" ,'.' , ":" ,";" ,'?' ,'(',')','[',']','&','!','*','@', '#','$','%' , '\\' , "'" ,'''"''','-','--']


file = open("IronyText_origin_Thread.txt")
try:
    allTheText = file.readlines()
finally:
    file.close()

for line in allTheText:
    for collocation in result_Irony:
        collocation[0] = collocation[0].lower()
        collocation[1] = collocation[1].lower()
        text = nltk.sent_tokenize(line)
        for sentence in text:
            if collocation[0] in sentence and collocation[1] in sentence:
                if collocation[0] in english_stopwords or collocation[0] in punctuation:
                     continue
                if collocation[1] in english_stopwords or collocation[1] in punctuation:
                     continue
                gram = str(collocation[1]) + " " + str(collocation[0])
                if gram == " " or "**" in gram:
                    continue
                hist_Irony[gram] = hist_Irony.get(gram,0) + 1

hist_Irony = sorted(hist_Irony.iteritems(),key = lambda d:d[1] , reverse = True)



file = open('Result_UnIrony_Dependency_Thread.txt')

try:
    allTheText = file.readlines()
finally:
    file.close()

result_Unirony = []
for line in allTheText:
    if line.find("nsubj")!= -1:
        line = line.replace("\n","").replace("nsubj","").replace("(","").replace(")","").replace("-","").replace(" ","")
        rule = re.compile("[0-9]")
        line = rule.sub("",line)

        result_Unirony.append(line.split(","))

file.close()


hist_top20_InUnirony = {}
for collocation in hist_Irony:
    gram = collocation[0]
    hist_top20_InUnirony[gram] = hist_top20_InUnirony.get(gram,0)
    for i in result_Unirony:
        temp = i[0] + " " + i[1]
        print temp
        if temp == gram:
            hist_top20_InUnirony[gram] = hist_top20_InUnirony.get(gram,0) + 1

print hist_top20_InUnirony



# result = ['videos','tho'],['others','go'],["republicans","holding"],["phone","call"],["theres","trash"],["lies","exposed"],["polister","predicted"],['article','question'],['costs','spiral'],['years','provides'],['parenting','provides'],['theyre','complicit'],['conservatives','call'],['action','institution.'],['moderates', 'kowtow'],['isnt','defunded'],['one','tells'],['problem','cooch'],['institutions' ,'forever'],['automation' ,'eliminated']

y = np.arange(0,20)
x1 = []
for i in range(0,20):
    x1.append(hist_Irony[i][1])

x2 = []
count = 1
yTicks = []
for i in hist_Irony:
    yTicks.append(i[0])
    x2.append(hist_top20_InUnirony[i[0]])
    count += 1
    if count == 21:
        break
print len(x2)

for i in range(len(x1)):
    #x1[i] = x1[i]/2590.0
    x1[i] = x1[i]/(1.0 *len(result_Irony))
for i in range(len(x2)):
    # x2[i] = x2[i]/(60528.0)
    print x2[i]
    x2[i] = x2[i]/(1.0 * (len(result_Unirony)))


plt.yticks(y,yTicks)
plt.ylabel('Word')
plt.xlabel('Frequency_Thread(Total Occurrences/Total Collocations)')
plt.plot(x1,y,'--or',label = 'Irony')
plt.plot(x2,y,'-ob' , label = 'UnIrony')
plt.legend()
plt.show()





#
#
#  *****************************************
#   以下为输出讽刺集中出现次数最多的程序
#  *****************************************

# file = open("IronyText_origin_Thread.txt")
# try:
#     allTheText = file.readlines()
# finally:
#     file.close()
#
# for line in allTheText:
#     for collocation in result_Irony:
#         collocation[0] = collocation[0].lower()
#         collocation[1] = collocation[1].lower()
#         text = nltk.sent_tokenize(line)
#         for sentence in text:
#             if collocation[0] in sentence and collocation[1] in sentence:
#                 if collocation[0] in english_stopwords or collocation[0] in punctuation:
#                      continue
#                 if collocation[1] in english_stopwords or collocation[1] in punctuation:
#                      continue
#                 gram = str(collocation[1]) + " " + str(collocation[0])
#                 if gram == " " or "**" in gram:
#                     continue
#                 hist_Irony[gram] = hist_Irony.get(gram,0) + 1

#
#
# # 图表形式输出
# X = np.arange(0,20)
# Y = []
# xTicks = []
# for i in range(0,20):
#     Y.append(hist_Irony[i][1])
#     xTicks.append(hist_Irony[i][0])
#
# plt.bar(X,Y,facecolor='#9999ff', edgecolor='white')
# plt.xticks(X,xTicks,rotation=90)
# plt.title("Analyze Phrase Collocation (Thread)")
#
# plt.show()
#
