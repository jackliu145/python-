import json

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s:%s" % (self.name, self.age)

stu = Student('jack', 22)

j = json.dumps(stu, default=lambda x : x.__dict__)
print(j)

stu2 = json.loads(j, object_hook=lambda x : Student(x['name'], x['age']))

print(stu2)
print(stu == stu2)

print(isinstance(stu2, Student))