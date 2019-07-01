import requests

r = requests.get('http://httpbin.org/cookies/set/number/12345677')
for key, value in r.cookies.items():
    print(key, ':', value)
print(r.text)

r = requests.get('http://httpbin.org/cookies')
for key, value in r.cookies.items():
    print(key, ':', value)
print(r.text)

s = requests.session()
r = s.get('http://httpbin.org/cookies/set/number/12345678979779')
for key, value in r.cookies.items():
    print(key, ':', value)
print(r.text)

r = s.get('http://httpbin.org/cookies')
for key, value in r.cookies.items():
    print(key, ':', value)
print(r.text)
