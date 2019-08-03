import requests
from lxml import etree

response = requests.get('https://juejin.im/post/5b94e93b5188255c672e901e')
# print(response.text)
html = etree.HTML(response.text)
# print(html.title())
title = html.xpath('//*[@id="juejin"]/div[2]/main/div/div[1]/article/h1/text()')
print(title)
article = html.xpath('//*[@id="juejin"]/div[2]/main/div/div[1]/article/text()')
print(article)