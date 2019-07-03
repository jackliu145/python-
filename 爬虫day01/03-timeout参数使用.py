import urllib.request
import socket


try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
    # print(response.read())
except socket.timeout as e:
    print('网络超时！')
