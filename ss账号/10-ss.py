import requests
from lxml import etree
import os
import re
import json
import io

# shadowsocks-libev配置

def get_ssr_item():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get('https://free.ishadowx.biz/', headers=headers)
    html = etree.HTML(response.text)

    cards = html.xpath(r'//div[@class="hover-text"]')
    for card in cards:
        item = {}
        ipAddr = item['server'] = ''.join(card.xpath('./h4[1]/span/text()')).strip()
        # 简单的过滤
        reg = re.compile(r'(\w+\.)+\w+') 
        if not reg.findall(ipAddr):
            continue
        item['server_port'] = int(''.join(card.xpath('./h4[2]/span/text()')).strip())
        item['password'] = ''.join(card.xpath('./h4[3]/span/text()')).strip()
        item['method'] = ''.join(card.xpath('./h4[4]/text()')).strip()[7:]
        item['local_port'] = 1080
        yield item

if __name__ == "__main__":
    items = list(get_ssr_item())
    with open('ss.json', 'w') as writer:
            writer.write(json.dumps(items[1], indent=4))
