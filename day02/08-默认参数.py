
# 默认参数

def my_power(x, y=2):
    n = 0
    sum = 1
    while n < y:
        sum *= x
        n += 1
    return sum

print(my_power(2, 3))
print(my_power(2))
