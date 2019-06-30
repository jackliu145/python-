import urllib.request
import http.cookiejar

cookies = http.cookiejar.MozillaCookieJar('cookie.txt')
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)

response = opener.open('https://www.baidu.com')
for item in cookies:
    print(item.name, ':', item.value)
cookies.save(ignore_discard=True, ignore_expires=True)
