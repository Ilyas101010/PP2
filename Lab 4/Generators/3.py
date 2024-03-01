def func(N):
    for i in range(0, N):
        if(i%3 == 0 and i%4 == 0):
            yield i

