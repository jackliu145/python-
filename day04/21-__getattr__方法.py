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

    def __getitem__(self, n):
        for x in range(n+1):
            self.__a, self.__b = self.__b, self.__a + self.__b
        return self.__a
    def __getattr__(self, n):   # 访问属性
        print('访问的属性为:', n)

Fib().name    # 
Fib().attr.gg.fsf.gg #