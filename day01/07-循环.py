names = ['jack', 'marry', 'tom', 'jerry']

for name in names:
    print(name)

names = (1, 2, 3)

for name in names:
    print(name)

# 计算0+1+2...+100的和
sum = 0
for num in range(1, 101):
    sum += num
print(sum)

sum = 0
n = 0
while n <= 100:
    sum += n
    n = n + 1
print(sum)

sum = 0
n = 0
while True:
    sum += n
    n += 1
    if n > 100:
        break
print(sum)
