from collections import defaultdict, OrderedDict

d = defaultdict(lambda : 'N/A')


print(d.get('key'))   # None
print(d['key'])    # 'N/A'


o = OrderedDict(dict(age=10, name='jack'))
print(o)
print(o.get('age'))
print(o['age'])
print(o.get('name'))

print(list(o.keys()))