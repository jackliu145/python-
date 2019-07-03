import urllib.request
import http.cookiejar

cookies = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookies)
openner = urllib.request.build_opener(handler)
response = openner.open('http://www.baidu.com')
for item in cookies:
    print(item.name, ':', item.value)