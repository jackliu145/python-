# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

# 再思考一下能否写出一个@log的decorator，使它既支持：
import functools

def log(call='call'):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args):
            print('before', call)
            result = fn(*args)
            print('after', call)
            return result
        return wrapper
    return decorator

@log()
def now(n):
    print('now', n)

@log('ddd')
def now2():
    print('hello')

now(1)
print(now.__name__)
now2()