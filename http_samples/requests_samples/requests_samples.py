# import requests

# # Get 请求
# r = requests.get('http://httpbin.org/get')
# print(r.status_code, r.reason)
# print('GET请求', r.text)

# # 带参数的 GET 请求
# r = requests.get('http://httpbin.org/get', params={'a': '1', 'b': '2'})
# print('带参数的 GET 请求', r.json())

# # POST 请求
# r = requests.post('http://httpbin.org/post', data={'a': '1'})
# print('POST 请求', r.json())

# # 自定义 headers 请求
# ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
#      'AppleWebKit/537.36 (KHTML, like Gecko) ' \
#      'Chrome/73.0.3683.86 Safari/537.36'
# headers = {'User-Agent': ua}
# r = requests.get('http://httpbin.org/headers', headers=headers)
# print('自定义 headers 请求', r.json())

# # 带 cookies 的请求
# cookies = dict(userid='123456', token='xxxxxxxxxxxxxxx')
# r = requests.get('http://httpbin.org/cookies', cookies = cookies)
# print('带cookies的请求', r.json())

# # Basic-auth 认证请求
# r = requests.get('http://httpbin.org/basic-auth/wg/123456', auth=('wg', '123456'))
# print('Basic-auth认证请求', r.json())

# # 主动抛出状态码异常
# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# bad_r.raise_for_status()

# # 使用 requests.Session 对象请求
# # 创建一个 Session 对象
# s = requests.Session()
# # session 对象会保存服务器返回的 set-cookies 头信息里面的内容
# s.get('http://httpbin.org/cookies/set/userid/123456')
# s.get('http://httpbin.org/cookies/set/token/xxxxxxx')
# # 下一次请求会将本地所有的 cookies 信息自动添加到请求头信息里面
# r = s.get('http://httpbin.org/cookies')
# print('检查session中的cookies', r.json())

# # 再 requests 中使用代理
# print('不使用代理：', requests.get('http://httpbin.org/ip').json())
# print('使用代理：', requests.get(
#     'http://httpbin.org/ip',
#     proxies={'http': 'http://122.51.236.106:41801'}
# ).json())

# # 延时爬取，再一定时间后爬取
# # 如果时间超过 timeout 会报 ReadTimeout 类型的错
# r = requests.get('http://httpbin.org/delay/4', timeout=5)
# print(r.text)

# 爬取网页的通用代码框架
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))