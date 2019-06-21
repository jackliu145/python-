try:
    f = open(r'D:python学习笔记\day06\hello.txt', 'r')
    
    print(f.read())
except BaseException as e:
    print(e)
finally:
    if f:
        f.close()