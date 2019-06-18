class Student(object):   # object 父类
    def __init__(this, name, score):    # 构造函数
        this.__name = name
        this.__score = score
    
    def print_score(self):
        print(self.__score)
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

tom = Student('Tom', 99)


tom.print_score()

# print(tom.__name)      # 无法访问，AttributeError: 'Student' object has no attribute '__name'
print(tom._Student__name)   # 获取__name属性，但是强烈建议不要这么做，不同解释器行为不一致。！！！！！
print(tom.get_name())
tom.set_name('Jack')
print(tom.get_name())
print(tom)  # 打印对象的地址