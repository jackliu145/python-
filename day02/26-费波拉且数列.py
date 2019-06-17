
def fib(num):
    a, b, n = 0, 1, 1

    while n < num:
        (a, b) = (b, a + b)
        yield a 
        n += 1

g = fib(6)

next(g)

for n in g:
    print(n)

# next(g)

