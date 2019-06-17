def triangles():
    p = [1]
    while True:
        p = [1] + [p[x] + p[x+1] for x in range(len(p)-1)] +[1]
        yield p

g = triangles()

count = 0;
for n in g:
    print(n)
    count += 1
    if count > 10:
        break