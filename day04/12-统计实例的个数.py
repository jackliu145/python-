class Student(object):
    count = 0

    def __init__(self):
        # Student.count += 1
        __class__.count += 1


stu = Student()
stu = Student()
stu = Student()
stu = Student()
stu = Student()

print(stu.count)
