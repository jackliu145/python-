age = input()
age = int(age)
if age <= 20:
    print('你的年龄为: %d' % age)
    print('是个年轻人了')
elif age <= 40:
 print('是个中年人啊')
 print('这个缩进会有问题吗？')
else:
    print('牛逼啊')

print('程序结束了')