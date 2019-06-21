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

# json.dumps(stu)   #  TypeError: Object of type Student is not JSON serializable

def student2dict(x):
    return {
        'name':x.name,
        'age': x.age
    }


l = json.dumps(stu, default=lambda x: {'name':x.name, 'age':x.age}) #ValueError: Circular reference detected

print(l)

# json.dumps(stu, default=student2dict)