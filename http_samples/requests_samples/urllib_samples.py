import urllib.request
import json

# 接受一个字符串作为参数
r = urllib.request.urlopen('http://httpbin.org/get')
# 读取 response 的内容
text = r.read()
# http 返回状态码和 massage
print(r.status, r.reason)
r.close()

# 返回的内容是json格式，直接用 Load 函数加载
obj = json.loads(text)
print(obj)

# r.headers 是一个 HTTPMessage 对象
# print(r.headers)
# 想要取所有的 headers
for k, v in r.headers._headers:
    print('%s: %s' % (k, v))

ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/73.0.3683.86 Safari/537.36'
# 添加自定义的头信息
req = urllib.request.Request('http://httpbin.org/user-agent')
req.add_header('User-Agent', ua)
# 接受一个urllib.request.Request 对象作为参数
r = urllib.request.urlopen(req)
resp = json.load(r)
# 打印出 httpbin 网站返回信息里的 user-agent
print("user-agent: ", resp["user-agent"])

# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='httpbin auth',
#                           uri='/basic-auth/wg/123456',
#                           user='wg',
#                           passwd='123456')
# opener = urllib.request.build_opener(auth_handler)
# urllib.request.install_opener(opener)
# r = urllib.request.urlopen('http://httpbin.org')
# print(r.read().decode('utf-8'))

# 使用 GET 参数
params = urllib.parse.urlencode({'spam': 1, 'egg': 2, 'bacon': 2})
url = 'http://httpbin.org/get?%s' % params
with urllib.request.urlopen(url) as f:
    print(json.load(f))

# 使用 POST 方法传递参数
data = urllib.parse.urlencode({'name': '小明', 'age': 2})
data = data.encode()
with urllib.request.urlopen('http://httpbin.org/post', data) as f:
    print(json.load(f))

# # 使用代理 IP 请求远程 url
# proxy_handler = urllib.request.ProxyHandler({
#                         'http': '182.35.85.44:9999'
#                     })
# # proxy_auth_handler = urllib.request.ProxyBasicAuthHandler() # 带用户名密码的使用这种
# opener = urllib.request.build_opener(proxy_handler)
# r = opener.open('http://httpbin.org/ip')
# print(r.read())

# urlparse 模块
# o = urllib.parse.urlparse()