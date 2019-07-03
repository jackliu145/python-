import urllib.request



url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/4.0',
    'Host' : 'httpbin.org'
}
params = {
    'name' : 'Germey'
}
data = bytes(urllib.parse.urlencode(params), 'utf8')
request = urllib.request.Request(url, data=data, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))