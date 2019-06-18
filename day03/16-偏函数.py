import functools

int2 = functools.partial(int, '1000', base=2)

print(int2())

def add(x, y):
    return x + y

add2 = functools.partial(add, 2, 2)

print(add2())