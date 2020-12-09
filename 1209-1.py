# -*- coding: utf-8 -*-
# @Time: 2020/12/09 14:46
# @Author: 李运辰
# @Software: PyCharm

# 导入requests包
import requests
from lxml import etree
import csv
import codecs
# 网页链接
url = "https://jobs.51job.com/pachongkaifa/p"
# 请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "guid=7e8a970a750a4e74ce237e74ba72856b; partner=blog_csdn_net",
    "Host": "jobs.51job.com",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

f = codecs.open('爬虫工程师岗位薪资.csv','a','gbk')
writer = csv.writer(f)
writer.writerow(["岗位","公司","城市","薪资"])

# 有请求头写法
for i in range(1,14):
    res = requests.get(url=url+str(i), headers=headers)
    res.encoding='gbk'
    s = res.text
    selector = etree.HTML(s)
    for item in selector.xpath('/html/body/div[4]/div[2]/div[1]/div/div'):
        title = item.xpath('.//p/span[@class="title"]/a/text()')
        name = item.xpath('.//p/a/@title')
        location_name = item.xpath('.//p/span[@class="location name"]/text()')
        sary = item.xpath('.//p/span[@class="location"]/text()')
        time = item.xpath('.//p/span[@class="time"]/text()')
        if len(title)>0 and  len(name)>0 and len(location_name)>0 and len(sary)>0 :
            print(title)
            print(name)
            print(location_name)
            print(sary)
            try:
                writer.writerow([title[0]+"",name[0]+"",location_name[0]+"",sary[0]+""])
            except:
                pass
            print("-----------")


f.close()