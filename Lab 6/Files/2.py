import os


print('Exist:', os.access(os.getcwd(), os.F_OK))
print('Readable:', os.access(os.getcwd(), os.R_OK))
print('Writable:', os.access(os.getcwd(), os.W_OK))
print('Executable:', os.access(os.getcwd(), os.X_OK))