class Fib(object):
    def __init__(self):
        self.__a = 0
        self.__b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if (self.__a > 100):
            raise StopIteration()
        return self.__a
g = Fib()

for a in g:
    print(a)