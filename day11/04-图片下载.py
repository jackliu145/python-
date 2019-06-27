import requests, re, threading, os
from urllib.parse import urlparse

dest = 'E:/hellocccc/'

def get_base_url(url):
    parse_result = urlparse(url)
    baseurl = parse_result.scheme + "://" + parse_result.netloc
    return baseurl

def get_home_page(home_page_url):
    r = requests.get(home_page_url)
    r.encoding = 'utf-8'
    # 首页标题的正则
    reg = r'<a\s+href=\"(/tupian/\w+\-[\u4e00-\u9fa5]{4}\.html)\"\s+target=\"_blank\">\s+([\u4e00-\u9fa5]{4})\s+</a>'
    result = re.findall(reg, r.text)
    baseurl = get_base_url(home_page_url)
    return [(baseurl + x, y) for x, y in result]

def enum_type_pic(pic_type_url, pic_type_name):
    r = requests.get(pic_type_url)
    r.encoding = 'utf-8'
    # 获取图片分类的超链接
    #  <li><a href="/tupian/59617.html" title="游戏或动漫同人CG725" target="_blank"><span>2019-06-26</span>游戏或动漫同人CG725</
    reg = r'<li><a\s+href=\"(/\w+/\d+\.html)\"\s+title=\"([0-9a-zA-Z\u4e00-\u9fa5]+)\"'
    result = re.findall(reg, r.text)
    baseurl = get_base_url(pic_type_url)
    # 修复url
    result2 = [(baseurl + x, y) for x, y in result]
    # 开启多线程下载图片吧
    for x in result2:
        t = threading.Thread(target=downloadpic, args = (*x, pic_type_name))
        t.start()
        # downloadpic(*x, pic_type_name)
    # 下一页
    next_page_reg = r'<a\s+href=\"(/tupian/list\-[\u4e00-\u9fa5]{4}\-\d*\.html)\"\s+title=\"\u4e0b\u4e00\u9875\">\u4e0b\u4e00\u9875</a>'
    next_page = re.findall(next_page_reg, r.text)
    print(next_page)
    if len(next_page) > 0:
        next_page_url = baseurl + next_page[0]
        print('进入下一页:',next_page_url)
        enum_type_pic(next_page_url, pic_type_name)
    # return [(baseurl + x, y) for x, y in result]

def downloadpic(url, pic_dir, pic_type_name):
    #拼接出本地磁盘的地址
    parentdir = os.path.join(dest, pic_type_name, pic_dir)
    if not os.path.exists(parentdir):
        os.makedirs(parentdir)
    r = requests.get(url)
    r.encoding = 'utf-8'

    # 获取图片超链接
    #  <img class="videopic lazy" src="/assets/images/default/loading/248x355.jpg" data-original="https://img.i1m2g3e.com/passimg/tp/59586/01.jpg"      
                #  title="咪咪小找不到固定男票好伤心1">
    reg = r'data-original=\"(https://.+)\"\s+title=\"[0-9a-zA-Z\u4e00-\u9fa5]+\"'
    result = re.findall(reg, r.text)
    for x in result:
        filename = os.path.basename(x)
        with open(os.path.join(parentdir, filename), 'wb') as f:
            f.write(requests.get(x).content)

    return result



def main():
    r = get_home_page(r'https://www.2019rx.com/index/home.html')
    for x in r:
        if x == r[0]:
            continue
        t = threading.Thread(target=enum_type_pic, args=(*x,))
        t.start()

main()