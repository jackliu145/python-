class Student(object):
    def __str__(self):
        return '打印这个实例, %s' % __class__
    

stu = Student()
stu.__str__()

print(stu)