def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x = 300

def myfunc():
    print(x)

myfunc()


x = 300 #global

def myfunc():
    x = 200 #local
    print(x)

myfunc()
print(x)


x = 300

def myfunc():
    global x
    x = 200

myfunc()
print(x)






