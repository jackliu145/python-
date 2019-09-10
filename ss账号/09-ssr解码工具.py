import base64
import json


config_str = r'{"log":{"loglevel":"warning"},"inbounds":[{"port":1080,"listen":"127.0.0.1","tag":"socks-inbound","protocol":"socks","settings":{"auth":"noauth","udp":false,"ip":"127.0.0.1"},"sniffing":{"enabled":true,"destOverride":["http","tls"]}}],"outbounds":[{"protocol":"shadowsocks","settings":{"servers":[{"address":"b.isxc.top","port":17998,"password":"isx.yt-28371051","method":"aes-256-cfb"},{"address":"c.isxc.top","port":13169,"password":"isx.yt-44267957","method":"aes-256-cfb"},{"address":"a.isxc.top","port":16455,"password":"isx.yt-16456189","method":"aes-256-cfb"},{"address":"c.isxb.top","port":11619,"password":"isx.yt-45213678","method":"aes-256-cfb"}]}}],"routing":{"domainStrategy":"IPOnDemand","rules":[{"type":"field","outboundTag":"direct","domain":["geosite:cn"]},{"type":"field","outboundTag":"direct","ip":["geoip:cn","geoip:private"]},{"type":"field","ip":["geoip:private"],"outboundTag":"blocked"},{"type":"field","domain":["geosite:category-ads"],"outboundTag":"blocked"}]},"dns":{"hosts":{"domain:v2ray.com":"www.vicemc.net","domain:github.io":"pages.github.com","domain:wikipedia.org":"www.wikimedia.org","domain:shadowsocks.org":"electronicsrealm.com"},"servers":["1.1.1.1",{"address":"114.114.114.114","port":53,"domains":["geosite:cn"]},"8.8.8.8","localhost"]},"policy":{"levels":{"0":{"uplinkOnly":0,"downlinkOnly":0}},"system":{"statsInboundUplink":false,"statsInboundDownlink":false}},"other":{}}'


def func1(item):
    return item.replace('-', '+').replace('_', '/')

def safe_base64_decode(s):
    left = len(s) % 4
    if left != 0:
        s += (left * b'=')
    return base64.b64decode(s)

def item2config(item):
    items = item.split(':')
    config = {
        "address": items[0],
        "port": int(items[1]),
        "method": items[3],
        "password": safe_base64_decode(items[5].split('/')[0].encode()).decode()
    }
    return config


def get_ssr_item():
    urls = 'ssr://MTM5LjI4LjIzNS4xMTY6MzMyNjpvcmlnaW46cmM0OnBsYWluOmJHNWpiaTV2Y21jZ09IWS8_b2Jmc3BhcmFtPSZyZW1hcmtzPTVyU2I1cDJKNTUtMlJBJmdyb3VwPVRHNWpiaTV2Y21j,ssr://MTM5LjI4LjIzNS4xMTc6MzMyNjpvcmlnaW46cmM0OnBsYWluOmJHNWpiaTV2Y21jZ09IWS8_b2Jmc3BhcmFtPSZyZW1hcmtzPTVyU2I1cDJKNTUtMlJRJmdyb3VwPVRHNWpiaTV2Y21j,ssr://MTM5LjI4LjIzNS4xMTg6MzMyNjpvcmlnaW46cmM0OnBsYWluOmJHNWpiaTV2Y21jZ09IWS8_b2Jmc3BhcmFtPSZyZW1hcmtzPTVyU2I1cDJKNTUtMlJnJmdyb3VwPVRHNWpiaTV2Y21j,ssr://NDUuMTI5LjIuMTcxOjMzMjY6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtY2dObU0vP29iZnNwYXJhbT0mcmVtYXJrcz02STZyNXBhdjU2ZVJRUSZncm91cD1URzVqYmk1dmNtYw,ssr://NDUuMTI5LjIuMTcwOjMzMjY6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtY2dObU0vP29iZnNwYXJhbT0mcmVtYXJrcz02STZyNXBhdjU2ZVJRZyZncm91cD1URzVqYmk1dmNtYw,ssr://NDUuMTI5LjIuMTcyOjMzMjY6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtY2dObU0vP29iZnNwYXJhbT0mcmVtYXJrcz02STZyNXBhdjU2ZVJRdyZncm91cD1URzVqYmk1dmNtYw,ssr://NS4xODAuNzcuNDY6MzMyNjpvcmlnaW46cmM0OnBsYWluOmJHNWpiaTV2Y21jZ05tNC8_b2Jmc3BhcmFtPSZyZW1hcmtzPTVMaWM1THFzUXcmZ3JvdXA9VEc1amJpNXZjbWM,ssr://NS4xODAuNzcuNDc6MzMyNjpvcmlnaW46cmM0OnBsYWluOmJHNWpiaTV2Y21jZ05tNC8_b2Jmc3BhcmFtPSZyZW1hcmtzPTVMaWM1THFzUkEmZ3JvdXA9VEc1amJpNXZjbWM,ssr://MTk0LjE1Ni4yMzAuMTE0OjMzMjY6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtY2dObTQvP29iZnNwYXJhbT0mcmVtYXJrcz01TGljNUxxc1dBJmdyb3VwPVRHNWpiaTV2Y21j,ssr://MTkzLjM4LjEzOS4yMzI6MzMyNjpvcmlnaW46cmM0OnBsYWluOmJHNWpiaTV2Y21jZ05tNC8_b2Jmc3BhcmFtPSZyZW1hcmtzPTVMaWM1THFzV1EmZ3JvdXA9VEc1amJpNXZjbWM,ssr://MTM5LjE4MC4xOTQuMjU0OjMzMjY6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtY2dObmcvP29iZnNwYXJhbT0mcmVtYXJrcz01cHUwNXBhd1F5M2t1NFhubEtqa3VvN29ycl9wbDY0Z1RHNWpiaTV2Y21jJmdyb3VwPVRHNWpiaTV2Y21j,ssr://MjA3LjE0OC4xMTEuMjQ4OjMzMjY6b3JpZ2luOnJjNDpwbGFpbjpiRzVqYmk1dmNtY2dObmcvP29iZnNwYXJhbT0mcmVtYXJrcz01cHUwNXBhd1JDM2t1NFhubEtqa3VvN29ycl9wbDY0Z1RHNWpiaTV2Y21jJmdyb3VwPVRHNWpiaTV2Y21j'
    aa = urls.split(',')
    aa = map(lambda item: item[6:], aa)
    aa = map(func1, aa)
    aa = map(lambda item: safe_base64_decode(item.encode()).decode('utf-8'), aa)
    # item2config(list(aa)[0])
    aa = map(item2config, aa)
    return aa
    
if __name__ == "__main__":
    items = list(get_ssr_item())
    print(items)
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

