s = set([1, 2, 3, 3, 4, 5])
print(s)   # 自动去重

s.add(1) # 添加一个元素，因为元素存在，所以s不受影响

s.add(100)

print(s) 

s.remove(2)   # 移除一个元素

# s.remove(2)   KeyError:2   元素不存在，移除报错

print(s)