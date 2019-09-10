import requests
from lxml import etree
import os
import re
import json
import io

# v2ray客户端配置

def get_ssr_item():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    # 如果网站被墙，开启代理
    # proxies={'http':'127.0.0.1:1087'}
    # response = requests.get('https://free.ishadowx.biz/', proxies=proxies, headers=headers)
    response = requests.get('https://free.ishadowx.biz/', headers=headers)
    html = etree.HTML(response.text)

    cards = html.xpath(r'//div[@class="hover-text"]')
    for card in cards:
        item = {}
        ipAddr = item['address'] = ''.join(card.xpath('./h4[1]/span/text()')).strip()
        # 简单的过滤
        reg = re.compile(r'(\w+\.)+\w+') 
        if not reg.findall(ipAddr):
            continue
        item['port'] = int(''.join(card.xpath('./h4[2]/span/text()')).strip())
        item['password'] = ''.join(card.xpath('./h4[3]/span/text()')).strip()
        item['method'] = ''.join(card.xpath('./h4[4]/text()')).strip()[7:]
        yield item

if __name__ == "__main__":
    items = list(get_ssr_item())
    # items = json.dumps(items, indent=4)
    with open('temp.json', 'r') as f:
        h = f.read()
        config = json.loads(h, encoding='utf-8')
        print(config['outbounds'])
        
        #  出口协议
        config['outbounds'] = [
            {
                'protocol': 'shadowsocks',
                'settings': {
                    'servers': items
                }
            },
            {
                "protocol": "freedom",
                "settings": {},
                "tag": "direct" 
            },
            {
                "protocol": "blackhole",
                "settings": {}
            }
        ]
        config['routing'] = {
            "domainStrategy": "IPOnDemand",
            "rules": [
            {
                "type": "field",
                "outboundTag": "direct",
                "domain": ["geosite:cn"] #中国大陆主流网站的域名
            },
            {
                "type": "field",
                "outboundTag": "direct",
                "ip": [
                "geoip:cn", #中国大陆的 IP
                "geoip:private" #私有地址 IP，如路由器等
                ]
            }
            ]
        }
        with open('config.json', 'w') as writer:
            writer.write(json.dumps(config, indent=4))
