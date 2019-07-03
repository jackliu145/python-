from pyquery import PyQuery

doc = PyQuery(url='https://www.baidu.com')

print(doc('input'))