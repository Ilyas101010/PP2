x = open('111.txt', 'a')
l = ['something', 'a', 12, 'Wow']

for i in l:
    x.write(str(i))
x = open('111.txt', 'r')
print (x.read())
x.close()
