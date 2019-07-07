import requests
from pyquery import PyQuery
from urllib import request
import threading
# requests.get('https://tetsai.net', p)

# doc = PyQuery(url='https://tetsai.net/')
# articles = doc('article')
# for article in articles.items():
#     print(article.text())
#     with open('123.txt', 'a+', encoding='utf-8') as f:
#         f.write(article.text())
#         f.write('\r\n' + '='*50 + '\r\n')

def hh():
    while True:
        requests.get('https://tetsai.net')

i = 0
while i < 30:
    threading.Thread(target=hh)

