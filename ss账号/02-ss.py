import requests
from lxml import etree
import os
import re
import json


def get_ssr_item():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get('https://vkuajing.net/free-ss/', headers=headers)

    html = etree.HTML(response.text)

    
    cards = html.xpath(r'//*[@id="post-1482"]/div[1]/div/div/div/div/div[2]//ul[1]')
    for card in cards:
        item = {
            "enable" : True,
            "password" : "yt-77570806",
            "method" : "aes-256-cfb",
            "remarks" : "",
            "server" : "a.isxb.top",
            "obfs" : "plain",
            "protocol" : "origin",
            "server_port" : 17497,
            }
        for server_ip in card.xpath('./li[2<=position() and position()<=3]/text()'):      
            item['server'] = server_ip
            item['server_port'] = int(''.join(card.xpath('./li[4]/text()')).split('：')[1])
            item['password'] = ''.join(card.xpath('./li[5]/text()')).split('：')[1]
            item['method'] = ''.join(card.xpath('./li[6]/text()')).split('：')[1]
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
    config["configs"] = list(get_ssr_item())
    # print(config)
    str = json.dumps(config, indent=4)
    print(str)
    with open('/Users/jack/Downloads/ss2.json', 'wb') as f:
        f.write(str.encode('utf8'))
