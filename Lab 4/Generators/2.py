n = int(input())

def gen(N):
    for i in range(0, n, 2):
        yield i

r = list(gen(n))
print (str(r))
