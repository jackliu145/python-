class Student(object):   # object 父类
    def __init__(self, name, score):    # 构造函数
        self.name = name
        self.score = score
    
    def print_score(self):
        print(self.score)


tom = Student('Tom', 99)
tom.print_score()
print(tom)  # 打印对象的地址