import requests
from urllib.parse import urlencode
import os
import threading

def get_home_page(offset, keyword):
    params = {
        "aid": 24,
        "app_name": "web_search",
        "offset": offset,
        "formart": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": 20,
        "en_qc": 1,
        "cur_tab": 1,
        "from": "search_tab",
        "pd": "synthesis",
        "timestamp": "1562682358709",
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://www.toutiao.com/",
        "scheme": "https",
        "cookie": r"tt_webid=6711307102394156551; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=16bd218dede7be-0e86a64579f94a-e343166-144000-16bd218dedf4b8; tt_webid=6711307102394156551; csrftoken=90ef5372643930a54ae5f4810b78a66f; CNZZDATA1259612802=1663894463-1562592929-%7C1562678743; __tasessionId=g6nqghfld1562682334323; s_v_web_id=69c089e09ace0418648e1fea98f2f6fb"
    }
    url = "https://www.toutiao.com/api/search/content" + "/?" + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if (response.status_code == 200):
            return response.json()
        return None
    except:
        return None
    
def parse_image(json):
    data = json.get('data')
    for image in  filter(lambda x: x.get('image_list') != None, data):
        item = {}
        item['title'] = image.get('title')
        item['image_list'] = image.get('image_list')
        yield item
    
def save_image(item):
    try:
        if not os.path.exists(item.get('title')):
            os.makedirs(item.get('title'))
    except :
        print(item.get('title') + '文件夹创建失败!!!')
        return None
    for image in item.get('image_list'):
        image_url = image.get('url')
        image_name = os.path.basename(image_url)
        if not image_name.endswith('.jpg'):
            image_name += '.jpg'
        filepath = os.path.join(item.get('title'), image_name)
        try:
            response = requests.get(image_url)
            print(dir(response))
        except:
            print('访问' + image_url + '请求网络失败')
            continue
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as f:
                f.write(response.content)
        else:
            print(image_name + '文件已经下载')

if __name__ == '__main__':
    for x in range(0, 100):
        r = get_home_page(x, "街拍")
        for item in parse_image(r):
            t = threading.Thread(target=save_image, args=(item,))
            t.start()
            # save_image(item)