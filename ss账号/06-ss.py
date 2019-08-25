import requests
from lxml import etree
import os
import re
import json
import io


config_str = r'{"log":{"loglevel":"warning"},"inbounds":[{"port":1080,"listen":"127.0.0.1","tag":"socks-inbound","protocol":"socks","settings":{"auth":"noauth","udp":false,"ip":"127.0.0.1"},"sniffing":{"enabled":true,"destOverride":["http","tls"]}}],"outbounds":[{"protocol":"shadowsocks","settings":{"servers":[{"address":"b.isxc.top","port":17998,"password":"isx.yt-28371051","method":"aes-256-cfb"},{"address":"c.isxc.top","port":13169,"password":"isx.yt-44267957","method":"aes-256-cfb"},{"address":"a.isxc.top","port":16455,"password":"isx.yt-16456189","method":"aes-256-cfb"},{"address":"c.isxb.top","port":11619,"password":"isx.yt-45213678","method":"aes-256-cfb"}]}}],"routing":{"domainStrategy":"IPOnDemand","rules":[{"type":"field","outboundTag":"direct","domain":["geosite:cn"]},{"type":"field","outboundTag":"direct","ip":["geoip:cn","geoip:private"]},{"type":"field","ip":["geoip:private"],"outboundTag":"blocked"},{"type":"field","domain":["geosite:category-ads"],"outboundTag":"blocked"}]},"dns":{"hosts":{"domain:v2ray.com":"www.vicemc.net","domain:github.io":"pages.github.com","domain:wikipedia.org":"www.wikimedia.org","domain:shadowsocks.org":"electronicsrealm.com"},"servers":["1.1.1.1",{"address":"114.114.114.114","port":53,"domains":["geosite:cn"]},"8.8.8.8","localhost"]},"policy":{"levels":{"0":{"uplinkOnly":0,"downlinkOnly":0}},"system":{"statsInboundUplink":false,"statsInboundDownlink":false}},"other":{}}'


def get_ssr_item():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
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
    config = json.loads(config_str, encoding='utf-8')
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
