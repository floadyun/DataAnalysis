# -*- coding: UTF-8 -*-
from snownlp import SnowNLP
import pandas as pd
import pylab as pl
txt = open('emotion', 'r', encoding='utf-8')
text = txt.readlines()
txt.close()
print('读入成功')
sentences = []
senti_score = []
for i in text:
    a1 = SnowNLP(i)
    a2 = a1.sentiments
    sentences.append(i)  # 语序...
    senti_score.append(a2)
    print('doing...', a2)
table = pd.DataFrame(sentences, senti_score)
# table.to_excel('F:/_analyse_Emotion.xlsx', sheet_name='Sheet1')
# ts = pd.Series(sentences, senti_score)
# ts = ts.cumsum()
# print(table)
x = [1, 2, 3, 4, 5, 6, 7, 8]
pl.mpl.rcParams['font.sans-serif'] = ['SimHei']
pl.title(u'心 灵 捕 手 网 评')
pl.xlabel(u'评 论 用 户')
pl.ylabel(u'情 感 程 度')
pl.plot(x, senti_score)
pl.show()