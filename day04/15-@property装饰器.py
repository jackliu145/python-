class Student(object):
    
    def __init__(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def name(self):
        return self.__name

stu = Student('Jack')
stu.score = 100

print(stu.score)

print(stu.name)

# stu.name = 'hello' AttributeError: can't set attribute 没有setter方法，变成了只读属性

