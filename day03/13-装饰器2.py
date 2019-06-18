import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            print(text)
            func(*args)
        return wrapper
    return decorator


@log('自定义文本')
def now(s):
    print(s)


now('fff')

print(now.__name__)