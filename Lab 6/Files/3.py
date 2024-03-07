import os

p = 'C:/Users/Asus/Desktop/PP2/'

if(os.path.exists(p)):
    file_name = os.listdir(p).pop()
    dir_list = os.listdir(p)
    print ("The file name: ", file_name)
    print ("All directories and files in the path: ", dir_list)
else:
    print('Path doesn\'t exist')

