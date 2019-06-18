
ll = [1, -1, 2, -3, -4, -100, 10, 98, 99, 80, 88]

l = sorted(ll, key=abs)
print(l)

print()


#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 请用sorted()对上述列表分别按名字排序：

names = sorted(L, key=lambda x: x[0].lower())
print(names)


# 再按成绩从高到低排序：
names = sorted(L, key=lambda x: -x[1])
print(names)