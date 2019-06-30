from urllib.request import build_opener, ProxyHandler

proxy_handler = ProxyHandler({
    'http' : 'http://127.0.0.1:1080',
    'https' : 'https://127.0.0.1:1080'
})

opener = build_opener(proxy_handler)
response = opener.open('https://www.google.com')
print(response)
print(response.read().decode('gbk'))