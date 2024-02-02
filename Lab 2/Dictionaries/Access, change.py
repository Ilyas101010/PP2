thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "blue", "black", "white"]
}
print(thisdict)
print(thisdict["brand"])
print(type(thisdict))

thisdict = dict(name = "john", age = 36, country = "Norway")
print(thisdict)

# access
x = thisdict["name"]

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

y = thisdict.get("2020")
print (y)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")



# change
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
thisdict.update({"year": 2020})

