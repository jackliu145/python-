import requests, re, os, threading
from urllib.parse import urlparse, urljoin

def mk_img_dir(*args):
    save_path = args[0]
    image_temp = args[1]
    if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
    with open(save_path, 'wb') as w:
        w.write(requests.get(image_temp).content)

def save_img(url):
    response = requests.get(url)
  
    # 使用正则表达式匹配所有的图片标签
    image_reg = r'<[img|IMG].*?src=[\'|\"](.*?(?:[\.jpg|\.jpeg|\.png|\.gif|\.bmp]))[\'|\"].*?[\/]?>'
    images = re.findall(image_reg, response.text)
  
    # 获取baseurl
    baseurl = urlparse(url).scheme + '://' + urlparse(url).netloc
    for image in images:
        image_temp = image
        # 修复路径
        if image.startswith('/'):
            image_temp = baseurl + image
        print('网络地址:', image_temp)
        image_url = urlparse(image)
        # 创建本地文件夹
        print(image_url.path)
        save_path = 'D:/pic2' + image_url.path
        print(save_path)
        # t = threading.Thread(target=mk_img_dir, args=(save_path, image_temp))
        # t.start()
        # if not os.path.exists(os.path.dirname(save_path)):
        #     os.makedirs(os.path.dirname(save_path))
        # with open(save_path, 'wb') as w:
        #     w.write(requests.get(image_temp).content)

    # 找到下一页按钮的url
    next_page_reg = r'<a href=[\'|\"](\w*\.html)[\'|\"]>\u4e0b\u4e00\u9875</a>'
    next_page = re.findall(next_page_reg, response.text)
    # print(next_page)
    if next_page:
        next_page_url = urljoin(url, next_page[0])
        print('进入下一页:',next_page_url)
        save_img(next_page_url)
    

# save_img('https://www.zbjuran.com/quweitupian/')
# https://www.zbjuran.com/mei/xinggan/201906/96304.html

# save_img('https://www.zbjuran.com/mei/xinggan/201906/96304.html')
# https://www.zbjuran.com/mei/xinggan/
# save_img('https://www.zbjuran.com/mei/xinggan/')


#没有下一页的就开始遍历页面中的图片连接
# <a target="_blank" href="/mei/xiaohua/201809/92511.html"></a>
url = r'https://www.zbjuran.com/mei/xinggan/'
response = requests.get(url)
pic_reg = r'<a\s+.*></a>'
pic_pages = re.findall(pic_reg, response.text)
for pic in pic_pages:
    pic_absolute_path = urljoin(url, pic)
    print(pic_absolute_path)  


