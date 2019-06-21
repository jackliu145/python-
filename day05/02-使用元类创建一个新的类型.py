
def __init__(self, name):
    self.__name = name

def print(self):
    # print(self.__name)
    print('hello')


NamePrint = type('NamePrint', (object, ), dict(print=print))

# n = NamePrint('Jack')
n = NamePrint()
n.print()

