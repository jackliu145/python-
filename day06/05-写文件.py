with open('test.txt', 'w', encoding='utf8') as f:
    f.write('这是一个文本文件')

with open('test.txt', 'r', encoding='utf8') as f:
    print(f.read())
