from collections.abc import Iterable, Generator
g = (x * x for x in range(11))

next(g)
print(next(g))
print(next(g))
print('***************************************8')
for x in g:
    print(x)

print(isinstance(g, Iterable))      #True
print(isinstance(g, Generator))   #True
print(g is g)
