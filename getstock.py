import re
import requests
from bs4 import BeautifulSoup
 
#获取html
def getHtml(url):
    try:
        req=requests.get(url)
        req.raise_for_status()
        req.encoding=req.apparent_encoding
        return req.text
    except :
        print('getHtml失败')
 
#获取股票代码
def getStockList(lst,stockUrl):
    html=getHtml(stockUrl)
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue
 
#获取股票详情
def getStockInfo(lst,stockUrl,fpath):
    count=0
    for stock in lst:
        url=stockUrl+stock+'.html'
        html=getHtml(url)
        try:
            if html=='':
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})
            name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList=stockInfo.find_all('dt')
            valueList=stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key=keyList[i].text
                val=valueList[i].text
                infoDict[key]=val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count+=1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count+=1
            print('\r当前速度e：{:.2f}%'.format(count*100/len(lst)),end='')
            continue
 
 
def main():
    stockListUrl='http://quote.eastmoney.com/stocklist.html'
    stockInfotUrl='https://gupiao.baidu.com/stock/'
    outPutFile='D:\python\shuju\stockInfo.txt'
    slist=[]
    getStockList(slist,stockListUrl)
    getStockInfo(slist,stockInfotUrl,outPutFile)
 
main()
