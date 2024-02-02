thisdict = {
   "a": 1,
   "b": 3,
   "c": 5
}

for x in thisdict:
    print(x)
    
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values(): #thisdict.keys():
    print(x)

for x, y in thisdict.items(): #both
    print(x, y)