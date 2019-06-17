t = (1, 2, [3, 4])

#s = set(t) TypeError: unhashable type: 'list' 报错
t2 = (1, 2, 3)
# s = set(t)

d = dict(t)
print(d)


s1 = []