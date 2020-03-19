from urllib.parse import urlparse
import os
from bs4 import BeautifulSoup
import requests

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

def parseHTMLPage(lst, html):
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.select("img"):
        if img.has_attr('src'):
            lst.append(img.attrs['src'])
        
    # for img in lst:
    #     print(img)

def downloadPics(lst, fpath):
    if not os.path.isdir(fpath):
        os.mkdir(fpath)

    for img in lst:
        o = urlparse(img)
        filename = o.path.split('/')[-1]
        filepath = os.path.join(fpath, filename)
        r = requests.get(img)
        print(img)
        with open(filepath, 'wb') as f:
            f.write(r.content)

def main():
    url = "http://www.yuhuagu.com/tzk/"
    lst = []
    fpath = os.path.join(os.curdir, 'images')
    # print(fpath)
    html = getHTMLText(url)
    parseHTMLPage(lst, html)
    downloadPics(lst, fpath)

main()