import requests 
import re
import json

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:] if len(item[3].strip()) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4].strip()) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }
def write_to_json(content):
    with open('result.txt', 'a') as f:
        f.write(json.dumps(content, ensure_ascii=False,) + ',\r\n')

def main():
    ulr = 'https://maoyan.com/board/4'
    html = get_one_page(ulr)
    for item in parse_one_page(html):
        write_to_json(item)

main()