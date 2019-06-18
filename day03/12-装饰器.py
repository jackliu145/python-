
# 装饰器，返回一个函数

def log(func):
    def wrapper(*args):
        print('Call %s' % func.__name__)
        func(*args)
    return wrapper


@log
def now(n):
    print('2019-6-18', n)


now({'name':'jack'})