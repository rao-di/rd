import requests
import urllib
from bs4 import BeautifulSoup, Tag, NavigableString
 
 
headers = {"Accept": "text/html, application/xhtml+xml, image/jxr, */*",
           "Accept - Encoding": "gzip, deflate, br",
           "Accept - Language": "zh - CN",
           "Connection": "Keep - Alive",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
           "referer":"baidu.com"}
 
org_word = 'HK公司'
url = "http://www.baidu.com/s?wd=" + urllib.parse.quote(org_word)
 
response = requests.get(url, headers=headers, timeout=120)
 
soup = BeautifulSoup(response.text,'lxml')
 
baike_citiao_mulu = soup.find_all('h3', class_='t')
for result_table in baike_citiao_mulu:  # result_table = baike_citiao_mulu[5]
    a_click = result_table.find("a")
    option_title = a_click.get_text()
    print("标题：" + a_click.get_text())  # 标题
    print("链接：" + str(a_click.get("href")))  # 链接
