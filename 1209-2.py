# -*- coding: utf-8 -*-
import csv
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
import jieba
import operator
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#岗位
title_list=[]
#城市
city_list=[]
#薪资分布
sary_list=[]

with open('爬虫工程师岗位薪资.csv','r',encoding = 'gbk') as fp:
    reader = csv.reader(fp)
    for row in reader:
        #岗位
        title_list.append(row[0])
        #城市
        city_list.append(row[2][0:2])
        #薪资分布
        sary = row[3].split("-")
        if(len(sary)==2):
            try:
                sary = sary[1].replace("/月","")
                if "万" in sary:
                    sary = sary.replace("万","")
                    sary = int(sary)
                    sary = sary*10000
                    sary_list.append(sary)
                if "千" in sary:
                    sary = sary.replace("千","")
                    sary = int(sary)
                    sary = sary * 1000
                    sary_list.append(sary)
            except:
                pass
#-----------可视化1：爬虫岗位常用名称-------
'''
dict_x = {}
for item in title_list:
    dict_x[item] = title_list.count(item)
sorted_x = sorted(dict_x.items(), key=operator.itemgetter(1), reverse=True)
k_list = []
v_list = []
for k, v in sorted_x[0:11]:
    k_list.append(k)
    v_list.append(v)
plt.axes(aspect=1)
plt.title(u'爬虫岗位常用名称(李运辰)')
plt.pie(x=v_list,labels= k_list,autopct='%0f%%')
plt.savefig("爬虫岗位常用名称.png", dpi=600)
plt.show()
'''
#------------可视化2：爬虫岗位最多的城市----------
'''
dict_x = {}
for item in city_list:
    dict_x[item] = city_list.count(item)
sorted_x = sorted(dict_x.items(), key=operator.itemgetter(1), reverse=True)
k_list = []
v_list = []
for k, v in sorted_x[0:11]:
    print(k, v)
    k_list.append(k)
    v_list.append(v)

plt.bar(k_list,v_list, label='爬虫岗位最多的城市')
plt.legend()
plt.xlabel('城市')
plt.ylabel('数量')
plt.title(u'爬虫岗位最多的城市(李运辰)')
plt.savefig("爬虫岗位最多的城市.png", dpi=600)
plt.show()
'''
#------------可视化3：薪资分布情况----------
'''
dict_x = {}
for item in sary_list:
    dict_x[item] = sary_list.count(item)
sorted_x = sorted(dict_x.items(), key=operator.itemgetter(1), reverse=True)
k_list = []
v_list = []
for k, v in sorted_x[0:15]:
    print(k, v)
    k_list.append(k)
    v_list.append(v)
plt.axes(aspect=1)
plt.title(u'薪资分布情况(李运辰)')
plt.pie(x=v_list, labels=k_list, autopct='%0f%%')
plt.savefig("薪资分布情况.png", dpi=600)
plt.show()
'''

data = pd.DataFrame({"value":sary_list})
cats1 = pd.cut(data['value'].values, bins=[8000, 10000, 20000, 30000, 50000,data['value'].max()+1])
pinshu = cats1.value_counts()
pinshu_df = pd.DataFrame(pinshu, columns=['频数'])
pinshu_df['频率f'] = pinshu_df / pinshu_df['频数'].sum()
pinshu_df['频率%'] = pinshu_df['频率f'].map(lambda x: '%.2f%%' % (x * 100))
pinshu_df['累计频率f'] = pinshu_df['频率f'].cumsum()
pinshu_df['累计频率%'] = pinshu_df['累计频率f'].map(lambda x: '%.4f%%' % (x * 100))
print(pinshu_df)
print()
print("李运辰")
