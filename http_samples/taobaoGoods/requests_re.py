import requests
import re

# 爬取淘宝商品信息定向爬虫

# 获取 HTML 页面
def getHTMLText(url):
    try:
        header = {
            'authority': 's.taobao.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'referer': 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'cna=+sk9FeyJHlMCAXuLiy5GYeUt; tracknick=%5Cu5927%5Cu4E70%5Cu5BB6lll; tg=0; miid=1463343868514609560; t=e8d895e4287b5734b0753b57a8a200c8; thw=cn; cookie2=17f8ae4cf5dc3b9cfc4399ac1eaca519; v=0; _tb_token_=fd51343636bf3; _samesite_flag_=true; sgcookie=EaqJtWI9AL0Sf%2F5E9Zyay; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dBxd7AQYzvLhxs39c%3D&nk2=1z8zU%2F2Bm9E0&id2=UoYZbYI%2BqLfMqg%3D%3D; csg=1a5e285d; lgc=%5Cu5927%5Cu4E70%5Cu5BB6lll; dnk=%5Cu5927%5Cu4E70%5Cu5BB6lll; skt=592d1ae163aad634; existShop=MTU4NDE1NjI0Nw%3D%3D; uc4=id4=0%40UO6Qps6xieYEqqngRLkYDaMUTEax&nk4=0%401fDIIlK62ULuM%2FtwxbhMFdw7Elo%3D; _cc_=Vq8l%2BKCLiw%3D%3D; enc=gJS2Ug%2B126PuBnKXEV37P9yUxC27op3tPyPUa4Tv4P%2FsRDXIKTrmc3O%2BNXuaaUW%2BC9bQ09G6oiAEqCaLSvclDw%3D%3D; tfstk=c1jhBn2xpw8QMS3rl2tCFq9k--4OZPaeOgSNbMm9HtqC4ajNihuZyz3_IBCh241..; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=1_1; JSESSIONID=AA9DA9DCA4E2C13D5B6FFBD1185E4CBB; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VT5L2FSpccLuJBreKQgf&existShop=false&pas=0&cookie14=UoTUPvImrqljnQ%3D%3D&tag=8&lng=zh_CN; isg=BPX1qz2ex9lwfiHoyaxeWBrWBHGvcqmEsjRzZXcdqmzSThBAOcG9VESMmBL4DsE8; l=dBLhmJhlv9rmE72DBOfNNsdt_ebT0BOfCsPzckixUICP9TCyOn0CWZqB80T2CnGVHsTJS37dYx9UBPYGcyCqJxpsw3k_J_Dq3dC..',
        }
        # 爬取淘宝遇到登陆问题解决方法：https://blog.csdn.net/Guanhai1617/article/details/104120581
        r = requests.get(url, timeout = 30, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

# 解析获取到的页面
# 参数：结果的列表类型和一个相关的html页面
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        print('plt长度', len(plt))
        # for i in range(len(plt)):
        #     print(plt[i])
        
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        print('tlt长度', len(tlt))
        # for i in range(len(tlt)):
            # print(tlt[i])
        for i in range(len(plt)):
            price = eval(plt[i].split(':', 1)[1])
            # print(price)
            title = eval(tlt[i].split(':', 1)[1])
            # print(title)
            ilt.append([price, title])
    except:
        print("")

# 输出结果信息
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 2 # 爬取的深度，也就是爬取到第几页
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    # 对每一页商品的 url 分别单独处理
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()

# import requests
# import re
 
# def getHtmlText(url):
#     try:
#         header =  {
#     'authority': 's.taobao.com',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'referer': 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200314&ie=utf8',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cookie': 'cna=+sk9FeyJHlMCAXuLiy5GYeUt; tracknick=%5Cu5927%5Cu4E70%5Cu5BB6lll; tg=0; miid=1463343868514609560; t=e8d895e4287b5734b0753b57a8a200c8; thw=cn; cookie2=17f8ae4cf5dc3b9cfc4399ac1eaca519; v=0; _tb_token_=fd51343636bf3; _samesite_flag_=true; sgcookie=EaqJtWI9AL0Sf%2F5E9Zyay; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dBxd7AQYzvLhxs39c%3D&nk2=1z8zU%2F2Bm9E0&id2=UoYZbYI%2BqLfMqg%3D%3D; csg=1a5e285d; lgc=%5Cu5927%5Cu4E70%5Cu5BB6lll; dnk=%5Cu5927%5Cu4E70%5Cu5BB6lll; skt=592d1ae163aad634; existShop=MTU4NDE1NjI0Nw%3D%3D; uc4=id4=0%40UO6Qps6xieYEqqngRLkYDaMUTEax&nk4=0%401fDIIlK62ULuM%2FtwxbhMFdw7Elo%3D; _cc_=Vq8l%2BKCLiw%3D%3D; enc=gJS2Ug%2B126PuBnKXEV37P9yUxC27op3tPyPUa4Tv4P%2FsRDXIKTrmc3O%2BNXuaaUW%2BC9bQ09G6oiAEqCaLSvclDw%3D%3D; tfstk=c1jhBn2xpw8QMS3rl2tCFq9k--4OZPaeOgSNbMm9HtqC4ajNihuZyz3_IBCh241..; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=1_1; JSESSIONID=41F88242B116C36D6511D88EFC01820E; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4plD&existShop=false&pas=0&cookie14=UoTUPvImrqliuQ%3D%3D&tag=8&lng=zh_CN; isg=BOPj3u7luac0cXceKxZQtpiscieN2HcacH5F8xVBnsK5VAJ2l6mUaoTGTiTadM8S; l=dBLhmJhlv9rmEwOLBOfZNsd9gFb9NIdb8sPzck_AUICPO41W5pXlWZqBWoLXCnGVHsG9r37dYx9UBkLFmyCqJxpsw3k_J_DmndC..',
# }
#         r = requests.get(url,headers = header)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
 
#         return r.text
#     except:
#         print("爬取失败")
#         return ""
    
    
# def parsePage(ilist,html):
#     try:
#         plt = re.findall(r'\"view_price\":\"\d+\.\d*\"',html)
#         tlt = re.findall(r'\"raw_title\":\".*?\"',html)
#         #print(tlt)
#         print(len(plt))
#         for i in range(len(plt)):
#             price = eval(plt[i].split('\"')[3])
#             title = tlt[i].split('\"')[3]
#             ilist.append([title,price])
#         #print(ilist)
#     except:
#         print("解析出错")
    
# def printGoodsList(ilist,num):
#     print("=====================================================================================================")
#     tplt = "{0:<3}\t{1:<30}\t{2:>6}"
#     print(tplt.format("序号","商品名称","价格"))
#     count = 0
#     for g in ilist:
#         count += 1
#         if count <= num:   
#             print(tplt.format(count,g[0],g[1]))
#     print("=====================================================================================================")
    
# def main():
#     goods = "篮球"
#     depth = 1
#     start_url = "https://s.taobao.com/search?q="+goods
#     infoList = []
#     num = 20
#     for i in range(depth):
#         try:
#             url = start_url + '$S=' + str(44*i)
#             html = getHtmlText(url)
#             print(html)
#             parsePage(infoList,html)
#         except:
#             continue
    
#     printGoodsList(infoList,num)
    
# main()