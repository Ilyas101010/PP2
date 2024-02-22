import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]

print(a)

import mymodule as mx
mx.greeting("Jonathan")

import platform

# built-in modules
x = platform.system()
print(x)

x = dir(mymodule)
print(x)

from mymodule import person1
