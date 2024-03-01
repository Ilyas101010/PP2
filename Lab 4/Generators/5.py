def func(n):
    for i in range(n, -1, -1):
        yield i

for i in func(10):
    print (i)
