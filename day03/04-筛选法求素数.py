
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() #初始化序列
    while True:
        first = next(it) # 返回第一个数
        yield first
        # it = filter(lambda y: y % first != 0, it)   这里有问题的，lambada表达式的坑，应该返回
        it = filter(_not_divisible(n), it) # 构造新序列


g = primes()

for n in g:
    if (n < 10):
        print(n)
    else:
        break
