from urllib import request
from urllib.parse import urlparse
import re
import os 

with request.urlopen(r'https://www.zbjuran.com/mei/xinggan/201906/96279.html') as f:
    data = f.read().decode('gbk')
    reg = r'<[img|IMG].*?src=[\'|\"](.*?(?:[\.jpg|\.jpeg|\.png|\.gif|\.bmp]))[\'|\"].*?[\/]?>'
    pic = re.findall(reg, data)
    
    for p in pic:
        if not p.startswith('http'):
            p =  'https://www.zbjuran.com' + p
        print('网络路径:', p)
        with request.urlopen(p) as f1:
            url = urlparse(f1.geturl())
            dest = os.path.join('D:', url.path)
            print('本机地址:', dest)
            parentdir = os.path.dirname(dest)
            try:
                os.makedirs(parentdir)
            except FileExistsError as e:
                pass
            with open(dest, 'wb') as d:
                d.write(f1.read())

            
            

