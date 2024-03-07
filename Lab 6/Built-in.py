# 1

arr = [1, 3, 5, 5, -1, -2]
s = 1
for i in range(0, len(arr)):
    s *= arr[i]
# print (s)
    
# 2

# s = input()
# cnt1 = 0 # lowercase
# cnt2 = 0 # uppercase

# for i in s:
#     if(i.islower()):
#         cnt1 += 1
#     else:
#         cnt2 += 1
# print (cnt1)
# print (cnt2)


# 3

# s = input()
# res = True
# s = s.lower()
# for i in range(0, len(s)//2):
#     if(s[i] != s[len(s)-1-i]):
#         res = False
#         print ("Not palindrome")
#         break

# if(res == True): print("Palindrome")


# 4

# from time import sleep
# import math


# def delay(fn, ms, *args):
#     sleep(ms / 1000)
#     return math.sqrt(fn)
# a = int(input())
# ms = int(input())
# print (f"The square root of {a} after {ms} miliseconds is", delay(a, ms))

# 5

s = [True, "cool", -1, 0, False, False]

print (all(s))