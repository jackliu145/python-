import urllib.request
import http.cookiejar

cookie = http.cookiejar.LWPCookieJar('cookie2.txt')
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)