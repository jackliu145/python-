from collections.abc import Iterable, Iterator

f = filter(lambda item: item % 2 == 1, range(100))

print(isinstance(f, Iterable))
print(isinstance(f, Iterator))

print(list(f))