# 1
def sq(N):
    for i in range(N): 
        yield i**2

for x in sq(6):
    print (x)


