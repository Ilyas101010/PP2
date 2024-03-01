def squares(a, b):
    for i in range(a, b+1):
        yield i**2

for i in squares(5, 10):
    print (i)

