import urllib.parse

result = urllib.parse.urlparse(r'http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result[0], result.scheme, sep='\n')

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
result = urllib.parse.urlunparse(data)
print(result)

result = urllib.parse.urlsplit(r'http://www.baidu.com/index.html;user?id=5#comment')
print(result)