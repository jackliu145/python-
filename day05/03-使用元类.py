def print123(self):
    print('hello')

MyClass = type('MyClass', (object, ),{'hello':print123} )


m = MyClass()
m.hello()