#1
def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

print(grams_to_ounces(100))

#2
def Celcius(fahr):
    return ((5/9)*(fahr - 32))
print(Celcius(-40))

#3
def solve(numheads, numlegs):
    rabbits = (numlegs - numheads * 2)//2
    chickens = numheads - rabbits
    print(rabbits, " rabbits and ", chickens, " chickens. ")

solve(35, 94)

#4
def filter_prime(nums):
    res = list()
    d = True
    for x in nums:
        if(x <= 2):
            res.append(x)
        else:
            for i in range(2, x):
                if(x % i == 0): 
                    d = False
                    break
            if(d == True): res.append(x)  
    return res

print(filter_prime([1, 2, 5, 7, 8, 8, 9, 10]))

#5
def permut(step, a):
    if(step == len(a)):
        print ("".join(a))
    for i in range(step, len(a)):
        a1 = [x for x in a]
        a1[step], a1[i] = a1[i], a1[step]

        permut(step + 1, a1)

permut(0, "abc")

#6
def rev_words(string):
    s = list(string.split(' '))
    s.reverse()
    res = ' '.join(s)
    return res
print(rev_words("We are ready"))

#7
# def has_33(arr):
#     for i in range(1, len(arr)-1):
#         if(arr[i-1] == arr[i] == 3 or arr[i] == arr[i+1] == 3):
#             return True
#     return False

# print(has_33([1, 3, 1, 7, 3]))

#8

def spy_game(arr):
    if(arr.count(0) < 2 or arr.count(7) == 0):
        return False
    else:
        string = ""
        zero_cnt = 0
        for i in arr:
            if(i == 0 and zero_cnt < 2):
                string += "0"
            if(i == 7): 
                string += "7"
            if(len(string) == 3): break
    if(string == "007"):
        return True
    else:
        return False

print (spy_game([1,2,4,0,0,7,5]))
print (spy_game([1,0,2,4,0,5,7])) 
print (spy_game([1,7,2,0,4,5,0]))


