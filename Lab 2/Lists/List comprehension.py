# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in fruits if x != "apple"]

print(newlist)

newlist = [x for x in range(10)  if x < 5]

print(newlist)

newlist = [x.upper() for x in fruits]

print(newlist)

newlist = ['hello' for x in fruits if x == 'apple']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != 'banana' else 'goodbye' for x in fruits]
print(newlist)
