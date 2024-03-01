import re
a = open("row.txt", "r", encoding= "UTF-8")
s = a.read()
print (s)

x = re.match(r"ab*?", s) #1
print (x)

x = re.match(r"ab{2,3}", s) #2
print (x)

s = "aa_bb gpgjFEFfpjgtrj AbEF. . , g_e"
x = re.findall(r"[a-z]+_[a-z]+", s) #3
print (x)

print(re.findall(r"[A-Z]+[a-z]+", s)) #4

print(re.match(r"a+?b$", s)) # 5

x = re.sub('[ ,.]', ":", s) # 6
print (x)

x = re.sub('_', '', s) # 7
print (x)

print(re.findall('[A-Z][^A-Z]*', s)) # 8

print(re.sub(r"(\w)([A-Z])", r"\1 \2", s)) #9
s = "CamelCaseString TestTest"
print(re.sub(r"(\w)([A-Z])+?([A-Z])?", r"\1_\2", s)) #10