from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, month in Month.__members__.items():
    print(name , '->', month)

print(dir(Month.__members__))