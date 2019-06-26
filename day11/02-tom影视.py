import requests, re, threading,os


dest = 'D:/hello143242/'

def gethomepage(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    # 首页标题的正则
    reg = r'<a\s+href=\"(/\w+/\w+\-[\u4e00-\u9fa5]{4}\.html)\"\s+target=\"_blank\">\s+[\u4e00-\u9fa5]{4}\s+</a>'
    result = re.findall(reg, r.text)
    # 这里后期优化，根据url动态截取出来，而不是写死
    baseurl = r'https://www.2019ug.com/'
    return [baseurl + x for x in result]

def enumtypepic(url):
    r = requests.get(url)
    r.encoding = 'utf-8'

    # 获取图片分类的超链接
    #  <li><a href="/tupian/59617.html" title="游戏或动漫同人CG725" target="_blank"><span>2019-06-26</span>游戏或动漫同人CG725</
    reg = r'<li><a\s+href=\"(/\w+/\d+\.html)\"\s+title=\"([0-9a-zA-Z\u4e00-\u9fa5]+)\"'
    result = re.findall(reg, r.text)
   
    # 这里后期优化，根据url动态截取出来，而不是写死
    baseurl = r'https://www.2019ug.com/'

    # 修复url
    result2 = [(baseurl + x, y) for x, y in result]
    # 开启多线程下载图片吧
    for x in result2:
        # print(x)
        t = threading.Thread(target=downloadpic, args = (x, ))
        t.start()

    # return [(baseurl + x, y) for x, y in result]

def downloadpic(url):
    # print(url)
    #拼接出本地磁盘的地址
    parentdir = dest + url[1]
    if not os.path.exists(parentdir):
        os.mkdir(parentdir)

    r = requests.get(url[0])
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
    r = gethomepage(r'https://www.2019ug.com/index/home.html')
    for x in r:
        t = threading.Thread(target=enumtypepic, args=(x,))
        t.start()


main()