import requests
from lxml import etree
from urllib.parse import urljoin
import os
import threading

def parse_home_page(url):
    '''
     输入色情网站的主页,解析网站的图片选项
    '''
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    for image_type in html.xpath('//*[@id="section-menu"]/div/div[3]/ul//a'):
        item = {}
        item['url'] = urljoin(url, image_type.xpath('./@href')[0])
        item['type'] = image_type.xpath('./text()')[0].strip()
        yield item

def parse_image_type(image_type):
    '''
    输入色情网站的选项卡的url，例如，自拍偷拍、亚洲色图，
    返回每个选项卡中的所有页面内容list
    '''
    image_url = image_type['url']
    response = requests.get(image_url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    for image_li in html.xpath('//*[@id="tpl-img-content"]/li'):
        item = {}
        item['type'] = image_type['type']
        item['title'] = image_li.xpath('./a/@title')[0]
        item['href'] = urljoin(image_url, image_li.xpath('./a/@href')[0])
        yield item
     # 递归下一页按钮
    next_page = html.xpath('//*[@id="main-container"]//div[@class="pagination"]/a[@title="下一页"]/@href')
    print('下一页', next_page)
    if next_page and next_page != 'javascript:;':
        try:
            for item in parse_img_type(urljoin(image_url, next_page[0])):
                yield item
        except: 
            return None
        

def parse_image_url(images):
    '''
    解析每种类型下的所有图片的list, list中包含图片所在页面
    '''
    # 创建文件加
    save_path = os.path.join('D:/456789', images['type'], images['title'])
    if not os.path.exists(save_path):
        os.makedirs(save_path)        
    # 获取图片
    response = requests.get(images['href'])
    response.encoding = 'utf-8'
    # print(response.text)
    html = etree.HTML(response.text)
    # 所有图片的src地址
    img_tags = html.xpath('//*[@id="main-container"]//div[@class="content"]/img/@data-original')
    for img in img_tags:
        img_name = os.path.join(save_path, os.path.basename(img))
        try:
            # with open(img_name, 'wb') as f:
            #     f.write(requests.get(img).content)
            #     print(img_name, '写入成功')
            t = threading.Thread(target=download_image, args=(img_name, img))
            t.start()
        except BaseException as e:
            print(e)
            continue
    # 下载图片

def download_image(save_path, url):
     with open(save_path, 'wb') as f:
        f.write(requests.get(url).content)
        print(save_path, '写入成功')

if __name__ == "__main__":
    for image_type in parse_home_page('https://www.69aff.com/index/home.html'):
        print('开始解析：' + image_type['type'])
        for images in parse_image_type(image_type):
            # parse_image_url(images)
            t = threading.Thread(target=parse_image_url, args=(images, ))
            t.start()
            pass
        









