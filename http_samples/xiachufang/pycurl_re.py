import re
import os
from io import BytesIO
from urllib.parse import urlparse
from pycurl import Curl

# pycurl 请求返回的是放在一个类似文件中，
# 此处的BytesIO就是一个放在内存中的文件，要把他放在一个真实的文件中
buffer = BytesIO()
c = Curl()
c.setopt(c.URL, 'http://www.xiachufang.com/')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
text = body.decode('utf-8')
print(text)

img_list = re.findall(r'src=\"(http://i5\.chuimg\.com/\w+\.jpg)', text)


# 初始化下载文件目录
image_dir = os.path.join(os.curdir, 'images')
# if not os.path.isdir(image_dir):
#     os.mkdir(image_dir)

for img in img_list:
    o = urlparse(img)
    filename = o.path[1:]
    filepath = os.path.join(image_dir, filename)
    # 有子目录的需要判断一下
    if not os.path.isdir(os.path.dirname(filepath)):
        os.mkdir(os.path.dirname(filepath))
    url = '%s://%s/%s' % (o.scheme, o.netloc, filename)
    print(url)
    with open(filepath, 'wb') as f:
        c = Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()