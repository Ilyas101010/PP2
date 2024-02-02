thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = set(("apple", "banana", "cherry"))

# access
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset) # check if in set


# add
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# remove
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
thisset.discard("banana") # no error if no such element exists

thisset.pop() # random item

thisset.clear() # empties the set

del thisset # deletes the set completely




