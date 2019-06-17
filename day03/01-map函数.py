def f(n):
    return pow(n, 2)

result = map(f, [1, 2, 3, 4, 5])

for n in result:
    print(n)