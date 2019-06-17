def append(L=[]):
    L.append('END')
    return L



print(append(['jack']))  # 正常调用没有问题

print(append())   # ['END']
print(append())   # ['END', 'END']  调用出了问题


# 将默认参数设置为不可变对象

def append_fixed(L =None):
    
    if L is None:
        L = []
    elif not isinstance(L, (list,)):
        raise TypeError('参数类型错误')
    L.append('END')
    return L



print(append_fixed(['jack']))  # 正常调用没有问题

# print(append_fixed('jack'))   # 参数类型错误
print(append_fixed())   
print(append_fixed())   
