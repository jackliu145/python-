import json

d = dict(name='jack', age=12)

r = json.dumps(d)

print(r)

d1 = json.loads(r)

print(d1)

print(d1 == d)   #True
print(d1 is d)   #False
print(d1 is d1)  # True
d1['name'] = 'Marry'
print(d1)
print(d)