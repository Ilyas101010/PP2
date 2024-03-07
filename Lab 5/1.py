import re

a = open('row.txt', 'r', encoding= "UTF-8").read()

s = re.findall(r"\w.+ мл|.+ фл", a)

print (s)