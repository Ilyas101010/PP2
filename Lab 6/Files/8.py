import os
p = 'C:/Users/Asus/Desktop/PP2/Lab 6/Files'

if (os.path.exists(p) == False):
    print ('Path doesn\'t exist')
else:
    os.remove('333.txt')
