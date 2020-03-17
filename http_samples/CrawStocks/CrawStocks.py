import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

# 在东方财富获取每个股票的代码，再去百度股票或者同花顺获取个股的详细信息
# 参数 lst 是获得的股票列表信息，stockURL是获取股票列表的url也就是东方财富的url
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            print('href', href)
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue
    print(len(lst))
    for i in range(len(lst)):
        print(lst[i])

# 获得每一支个股的股票信息
# 参数 1、保存所有股票的信息列表 2、获得股票信息的url网站 3、以及要把信息存进文件的文件路径
def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keylist = stockInfo.find_all('dt')
            valuelist = stockInfo.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                infoDict[key] = val
            
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()
            continue

def main():
    # 获取股票列表的链接
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    # 获取个股信息的链接
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    fpath = '/home/wg/GitHub/python/http_samples/CrawStocks/CrawStock.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, fpath)

main()