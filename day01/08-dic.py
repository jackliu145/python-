scores = {'jack':90, 'marry':80, 'tom':70}
print(scores['jack'])
print(scores.get('jack'))
print('jack' in scores)   # 判断是否存在该键
# print(scores['jjj'])  KeyError: 'jjj'
print(scores.get('jjjj'))   # 打印 None
print(scores.pop('jack'))  # 删除一个元素
print(scores)


# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。