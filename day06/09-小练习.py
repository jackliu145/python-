# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os

def list_rec(p, filename):
    if not os.path.isdir(p) :
        # if str(p).find(filename) != -1:
        print(p)
    else:
        for x in os.listdir(p):
            list_rec(os.path.abspath(os.path.join(p, x)), filename)

list_rec('C:\\windows', 'notepad')


