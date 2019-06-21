import os
from os import path

# for x in dir(os):
#     if callable(x):
#         x()
#     else:
#         print(x)

print(os.name)
print(os.pardir)
print(path.join('hello', 'world'))  # 路径拼接
print(path.splitext(r'C:\Windows\system.ini'))    #返回一个tuple， ('C:\\Windows\\system', '.ini')
print(path.splitdrive(r'c:\Windows\system.ini'))   #('c:', '\\Windows\\system.ini')
print(path.split(r'c:\Windows\system.ini'))

print([x for x in os.listdir('.')])