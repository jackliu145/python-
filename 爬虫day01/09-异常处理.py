import urllib.request
import urllib.error

try:
    urllib.request.urlopen('http://cuiqingcai.com/index.htm')
except urllib.error.URLError as e:
    print(e.reason)