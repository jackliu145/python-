def foo(n):
    assert n != 0, 'n不能为0'
    return 10 / n


foo(1)
foo(0)