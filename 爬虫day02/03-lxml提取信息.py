import requests 
from lxml import etree


response = requests.get('https://www.rupeng.com/')
response.encoding = 'utf8'
html = etree.HTML(response.text)
title = html.xpath('//title/text()')
print(title)
# print(etree.tostring(html).decode('utf8'))