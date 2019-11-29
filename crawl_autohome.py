#!/usr/bin/env python
# coding:utf-8

import requests
from bs4 import BeautifulSoup

# 1.下载页面
ret = requests.get(url="https://www.autohome.com.cn/news/")
# print(ret) # 得到对象
# ret.encoding="gbk" # 指定编码
# print(ret.apparent_encoding)
ret.encoding = ret.apparent_encoding  # 指定编码等于原始页面编码
# print(ret.text)


# 2. 解析：获取想要的指定内容 beautifulsoup
soup = BeautifulSoup(ret.text, 'html.parser')  # 使用lxml则速度更快

# 如果要加class,则前面加下划线
# div = soup.find(name='div', id='auto-channel-lazyload-article', _class='article-wrapper')  # 找到外部DIV
div = soup.find(name='div', attrs={"id":"auto-channel-lazyload-article","class":"article-wrapper"})  # 使用属性字典方式

li_list = div.find_all(name='li')

for li in li_list:
    h3 = li.find(name='h3')
    if not h3:
        continue
    print(h3.text)

    a = li.find('a')
    # print(a.attrs)
    print(a.get('href'))

    p = li.find(name='p')
    print(p.text)
    print('----->' * 20)

    img = li.find(name='img')
    src = img.get('src')

    filename = src.rsplit('__', maxsplit=1)[1]

    down_img = requests.get(url='https:' + src)
    with open(filename, 'wb') as f:
        f.write(down_img.content)
