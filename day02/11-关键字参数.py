def printkw(**kw):  # kw会被转换成dic类型

    if isinstance(kw, (dict,)):
        print('kw is dic')
    print(kw)
    pass

printkw(hello='jack')  

keys = {'name':'jack', 'age':12}

printkw(**keys)