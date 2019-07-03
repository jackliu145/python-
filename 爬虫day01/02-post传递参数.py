import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'world':'hello'}), 'utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf8'))