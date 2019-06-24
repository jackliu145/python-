from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x)
print(p.__str__())
print(isinstance(p, tuple))