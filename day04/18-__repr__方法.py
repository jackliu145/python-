
class Student(object):
    def __repr__(self):
        return "打印出来的字符串"
    __str__ = __repr__  #通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法


stu = Student()

stu # 控制台打印__repr__函数调用返回的结果
