import json

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s:%s" % (self.name, self.age)

stu = Student('jack', 22)
print(stu)

stu.name = 'Marry'
stu.age = 23

print(stu)


l = json.dumps(stu, default=lambda x : x.__dict__) 

print(l)

