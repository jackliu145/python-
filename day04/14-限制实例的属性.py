# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

class Student(object):
    __slots__ = ('name', 'age')


stu = Student()
stu.name = 'jack'
print(stu.name)

# stu.addr = 'hubei'     AttributeError: 'Student' object has no attribute 'addr'
# print(stu.addr)


class BoyStudent(Student):    # 如果派生类没有设置__slots__属性，基类的__slots__不会限制派生类
    pass

bs = BoyStudent()
bs.name = 'jack'
print(bs.name)  

bs.addr = 'hubei'
print(bs.addr)   


class GirlStudent(Student):
    __slots__ = ('hobby',)

gs = GirlStudent()
gs.name = 'Marry'              # 派生类会继承基类的__slots__属性
print(gs.name)

# gs.addr = 'hubei'  AttributeError: 'Student' object has no attribute 'addr'
