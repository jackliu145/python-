try:
    i = 1 / 0
    print('继续跑')
except ZeroDivisionError as e:
    print(e)
finally:
    print('反正我会执行')