import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

# r = requests.get('https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155&page=2')
# print(r.json().get('data').get('cards')[0])

client = MongoClient()
db = client['weibo']
collection = db['weibo']
max_page = 14

def get_page(page):
    headers = {
        'Referer': 'https://m.weibo.cn/u/2145291155',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    # type=uid&value=2145291155&containerid=1076032145291155&page=2
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }
    url = 'https://m.weibo.cn/api/container/getIndex?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.json()
    except:
        return None

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        print(items)
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            more = pq(item['text'])('a')
            if more:
                print('有查看全部', more.attr.href)
            weibo['reposts_count'] = item.get('reposts_count')
            weibo['comments_count'] = item.get('comments_count')

            weibo['attitudes_count'] = item.get('attitudes_count')
            yield weibo


if __name__ == "__main__":
    for i in range(1, 2):
        json = get_page(i)
        items = parse_page(json)
        for item in items:
            print(item)

