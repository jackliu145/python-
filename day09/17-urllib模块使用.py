from urllib import request
import re

with request.urlopen(r'https://www.zbjuran.com/mei/xinggan/201906/96279.html') as f:
    print(dir(f))
    data = f.read().decode('gbk')
    reg = r'<[img|IMG].*?src=[\'|\"](.*?(?:[\.jpg|\.jpeg|\.png|\.gif|\.bmp]))[\'|\"].*?[\/]?>'
    pic = re.findall(reg, data)
    for p in pic:
        print(p)