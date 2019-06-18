def func():
    def sum(n):
        a = 0
        for x in n:
            a += x
        return a
    return sum

ff = func()

print(ff)

print(ff([1, 2, 3, 4]))