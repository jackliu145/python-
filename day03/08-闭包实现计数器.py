
def createCounter():
    n = [0]     # 不能用变量 变量会被覆盖
    def counter(): 
        n[0] += 1   
        return n[0]
    return counter



counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')