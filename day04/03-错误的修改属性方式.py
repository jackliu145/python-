class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

tom = Student('Tom', 22)

print(tom.get_name())    # Tom
# print(tom.__name)  这里会报错，没有该属性  因为类中的私有属性已经被解释器改名成_Student__name了

tom.__name = 'Jack'   # 这里不会修改Tom的类中的__name私有属性， 而是会添加一个tom实例__name属性
print(tom.get_name())   # 'tom'  

tom.set_name('Marry')
print(tom.get_name())