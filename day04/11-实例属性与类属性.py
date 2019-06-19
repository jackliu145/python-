class Student(object):
    name = 'Student'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

stu  = Student('jack', 22)
print(stu.name)   #  jack
print(Student.name)  #  Student

del stu.name
print(stu.name)   # 类的属性会暴露出来