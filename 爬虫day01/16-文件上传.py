import requests

files = {'file': open('favorite.ico', 'rb')}

r = requests.post('http://httpbin.org/post', files=files)
print(r.status_code)
print(r.text)
print(r.cookies)
for key, value in r.cookies.items():
    print(key, ':', value)