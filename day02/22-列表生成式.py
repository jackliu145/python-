# 生成一个1X1, 2X2, ..., 99 X 99 的列表

L = [n * n for n in range(100)]

print(L)

# 生成一个偶数的平方


L = [ n * n for n in range(100) if n % 2 == 0]
print(L)
a = 1
b = 2
(a, b) = (b, a)
print(a, b)