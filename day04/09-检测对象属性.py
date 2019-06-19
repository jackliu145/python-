
class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def print(self):
        print(self.__name)

stu = Student('jack', 22)
 
print(hasattr(stu, 'name'))     # False
print(hasattr(stu, '__name'))   # False
print(hasattr(stu, '_Student__name'))  # True
print(hasattr(stu, 'age'))    # True

print(getattr(stu, 'age'))   # 22
# print(getattr(stu, 'name'))  报错AttributeError: 'Student' object has no attribute 'name'
print(getattr(stu, 'name', '默认名字'))   # 默认名字

setattr(stu, 'name', 'Tom')  
print(stu.name)     # 该属性是上一个方法添加的，不是类中的

# 获取对象的方法
fn = stu.print
fn()

