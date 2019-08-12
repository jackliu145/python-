import requests
from lxml import etree
import os
import re
import json


def get_ssr_item():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    proxies={'http':'127.0.0.1:1087'}
    response = requests.get('https://free.ishadowx.biz/', proxies=proxies, headers=headers)

    html = etree.HTML(response.text)

    # //*[@id="portfolio"]/div[2]/div[2]/div/div[1]
    cards = html.xpath(r'//div[@class="hover-text"]')
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
        ipAddr = item['server'] = ''.join(card.xpath('./h4[1]/span/text()')).strip()
        # 简单的过滤
        reg = re.compile(r'(\w+\.)+\w+') 
        if not reg.findall(ipAddr):
            continue
        item['server_port'] = int(''.join(card.xpath('./h4[2]/span/text()')).strip())
        item['password'] = ''.join(card.xpath('./h4[3]/span/text()')).strip()
        item['method'] = ''.join(card.xpath('./h4[4]/text()')).strip()[7:]
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
    with open('/Users/jack/Downloads/ss.json', 'wb') as f:
        f.write(str.encode('utf8'))
