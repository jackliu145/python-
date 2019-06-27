import requests, re, threading, os
from urllib.parse import urlparse
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dest = 'D:/hellocccc/'

def initDb():
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test?charset=utf8', encoding='utf-8', echo=True)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def close(session):
    # 提交即保存到数据库:
    session.commit()
    session.close()

# 创建对象的基类:
Base = declarative_base()
session = initDb()

class Pic(Base):
    # 表的名字:
    __tablename__ = 't_pic'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    pic_name = Column(String(255))
    pic_dir = Column(String(255))
    pic_type_name = Column(String(255))
    url = Column(String(255))
    

def savePic(url, pic_name, pic_dir, pic_type_name):
    '''保存图片信息到数据库中 
    '''
    pic = Pic(id=None, pic_name=pic_name, pic_dir=pic_dir, pic_type_name=pic_type_name, url=url)
    session.add(pic)
    # print(url, pic_dir, pic_type_name)
    session.commit()
    pass

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
        # t = threading.Thread(target=downloadpic, args = (*x, pic_type_name))
        # t.start()
        downloadpic(*x, pic_type_name)
        

    # return [(baseurl + x, y) for x, y in result]

def downloadpic(url, pic_dir, pic_type_name):
    #拼接出本地磁盘的地址
    parentdir = os.path.join(dest, pic_type_name, pic_dir)
    if not os.path.exists(parentdir):
        os.makedirs(parentdir)
    print(parentdir)
    r = requests.get(url)
    r.encoding = 'utf-8'

    # 获取图片超链接
    #  <img class="videopic lazy" src="/assets/images/default/loading/248x355.jpg" data-original="https://img.i1m2g3e.com/passimg/tp/59586/01.jpg"      
                #  title="咪咪小找不到固定男票好伤心1">
    reg = r'data-original=\"(https://.+)\"\s+title=\"[0-9a-zA-Z\u4e00-\u9fa5]+\"'
    result = re.findall(reg, r.text)
    for x in result:
        filename = os.path.basename(x)
        # 打印url, 名称, 文件夹, 类别
        savePic(x, filename, pic_dir, pic_type_name)
        # with open(os.path.join(parentdir, filename), 'wb') as f:
        #     f.write(requests.get(x).content)

    return result



def main():
    r = get_home_page(r'https://www.2019rx.com/index/home.html')
    # for x in r:
    #     t = threading.Thread(target=enum_type_pic, args=(*x,))
    #     t.start()
    for x in r:
        enum_type_pic(*x)

main()