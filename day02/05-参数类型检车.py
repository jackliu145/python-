def my_abs(x):
    if not isinstance(x, (float, int)):
        raise TypeError('参数类型错误')
    if x >= 0:
        return x
    else:
        return -x

def my_abs_without_type_check(x):
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs('A'))
print(my_abs(-1))

# print(my_abs_without_type_check('A'))  TypeError: '>=' not supported between instances of 'str' and 'int'