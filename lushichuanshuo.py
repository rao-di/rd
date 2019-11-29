import os
import requests
from bs4 import BeautifulSoup
import time
# 发送请求
def send():
    r = requests.get(url=base_url)
    # 设置编码防止乱码
    r.encoding ="GBK";
    content = r.text
    parseAndSave(content)
# 解析页面和保存数据
def parseAndSave(html):
    soup = BeautifulSoup(html, 'lxml')
    ulList = soup.find_all('ul', attrs={'class': 'kzlist'})
    # print(ulList);
    for ul in ulList:
        li = ul.find_all('li');
        for item in li:
            name  = item.find('img').next_sibling
            obtain_method  = item.find('a').find('p').text
            rootDir = os.getcwd()
            if not os.path.exists(name):
                os.mkdir(name);
                os.chdir(name);
                src = item.find('a').find('img')['src']
                pic = requests.get(src)
                with open('pic.jpg', 'wb') as fw:
                      fw.write(pic.content)
                with open('info.txt', 'a+') as fw:
                      fw.write(name+'\n')
                      fw.write(obtain_method)
                os.chdir(rootDir);
def main():
    start_time = time.time()
    send()
    end_time = time.time()
    print('程序用时：',(end_time - start_time))
if __name__ == '__main__':
    base_url = 'http://news.4399.com/gonglue/lscs/kabei/'
    cardList = []
    main()
