from types import MethodType

class Student(object):
    pass



stu = Student()

def set_age(self, age):
    self.__age = age

def get_age(self):
    return self.__age


stu.set_age = MethodType(set_age, stu)   # 绑定要给实例方法

stu.set_age(123)

stu.get_age = MethodType(get_age, stu)
print(stu.get_age())


#给class绑定新方法
def set_name(self, name):
    self.__name = name

def get_name(self):
    return self.__name

Student.set_name = set_name
Student.get_name = get_name

stu.set_name('jack')  
print(stu.get_name())  

stu2 = Student()
stu2.set_name('jack')
print(stu2.get_name())