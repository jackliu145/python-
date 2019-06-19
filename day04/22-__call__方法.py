class Student(object):
    def __call__(self):
        print("实例被调用了")


stu = Student()
stu()

print(callable(stu))
print(callable(int))
print(callable('123'))