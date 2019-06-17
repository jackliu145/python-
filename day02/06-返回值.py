import math

# 返回一个坐标值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(1, 2, 3)

print('x =', x)
print('y =', y)