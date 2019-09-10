import requests
from lxml import etree
import os
import re
import json


def get_ssr_item():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    # 如果网站被墙，开启代理
    # proxies={'SOCKS5':'127.0.0.1:1080'}
    my_proxies={"socks5:":"socks5://127.0.0.1:1080","https":"socks5://127.0.0.1:1080"}
    response = requests.get('https://www.youneed.win/free-ssr', proxies=my_proxies, headers=headers)
    html = etree.HTML(response.text)
    trs= html.xpath(r'//div//table//tr')
    trs = trs[1:]
    for tr in trs:
        td = tr.xpath(r'.//td/text()')
        print(len(td))
        if len(td) != 6:
            continue
        item = {
            "enable" : True,
            "password" : td[2],
            "method" : td[3],
            "remarks" : "",
            "server" : td[0],
            "obfs" : td[5],
            "protocol" : td[4],
            "server_port" : int(td[1]),
            }
        print(item)
        yield item

if __name__ == "__main__":
    config = {
        "random": False,
        "authPass": None,
        "useOnlinePac": False,
        "TTL": 0,
        "global": False,
        "reconnectTimes": 3,
        "index": 0,
        "proxyType": 0,
        "proxyHost": None,
        "authUser": None,
        "proxyAuthPass": None,
        "isDefault": False,
        "pacUrl": None,
        "configs": [
        ],
        "proxyPort": 0,
        "randomAlgorithm": 0,
        "proxyEnable": False,
        "enabled": True,
        "autoban": False,
        "proxyAuthUser": None,
        "shareOverLan": False,
        "localPort": 1080
        }
    # config["configs"] = 
    print(list(get_ssr_item()))
    # print(config)
    # str = json.dumps(config, indent=4)
    # with open('/Users/jack/Downloads/ss.json', 'wb') as f:
    #     f.write(str.encode('utf8'))
