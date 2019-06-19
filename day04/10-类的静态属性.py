class Student(object):
    count=0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
stu = Student('Jack', 22)
stu2 = Student('Tom', 23)

print(stu.count)
print(stu2.count)
print(Student.count)