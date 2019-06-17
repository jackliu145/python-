
# 声明 函数时，如果函数的参数为可变参数，形参前面加一个*

# 调用函数时，如果函数的参数为可变参数，传入list或者cuple实参时，list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

def my_print(*numbers):
    for num in numbers:
        print(num)
    pass

my_print(1, 2, 3)

numbers = (1, 2, 3)
my_print(*numbers)