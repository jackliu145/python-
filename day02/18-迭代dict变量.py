d = {
    'name':'jack',
    'age':12,
    'addr':'huber'
}

# 迭代dict类型元素
for k, v in d.items():
    print('%s:%s' % (k, v))

for k in d:
    print('key :', k)


for v in d.values():
    print('value :', v)