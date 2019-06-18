# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数

def is_palindrome(n):
    f = filter(lambda x: x == int(str(x)[::-1])  ,range(n))
    return list(f)

result = is_palindrome(10000)
print(result)

# 切片
s = '123434566'
print(s[::-1])
print(s[:])
print(s[:-1])
print(s[::2])