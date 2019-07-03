import requests
params = {
    'name' : 'jack',
    'age' : 17
}
r = requests.get('http://httpbin.org/get', params=params)
print(r.text)
print(r.json())
print(type(r.json()))