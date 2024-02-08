#1
def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

#2
def Celcius(fahr):
    return ((5/9)*(fahr - 32))


#3
def solve(numheads, numlegs):
    rabbits = (numlegs - numheads * 2)//2
    chickens = numheads - rabbits
    print(rabbits, " rabbits and ", chickens, " chickens. ")


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

#5
def permut(step, a):
    if(step == len(a)):
        print ("".join(a))
    for i in range(step, len(a)):
        a1 = [x for x in a]
        a1[step], a1[i] = a1[i], a1[step]

        permut(step + 1, a1)

#6
def rev_words(string):
    s = list(string.split(' '))
    s.reverse()
    res = ' '.join(s)
    return res

#7
def has_33(arr):
    for i in range(1, len(arr)-1):
        if(arr[i-1] == arr[i] == 3 or arr[i] == arr[i+1] == 3):
            return True
    return False

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

# 9
import math
def volume_sphere(R):
    return 4/3*math.pi*R**3

# 10
def unique(abc):
    new_abc = []
    for x in abc:
        if(x not in new_abc):
            new_abc.append(x)
    return new_abc

# 11
def is_palindrome(string):
    for i in range(0, len(string)//2):
        if(string[i] != string[len(string)-1-i]):
            return False
    return True

# 12
def histogram(a):
    for x in a:
        print ("*"*x)

# 13


def guess_game(cnt, num):
    print ("Hello! What is your name?")
    name = input()
    txt = "Well, {}, I am thinking of a number between 1 and 20."
    print (txt.format(name))

    x = -1
    print("Take a guess.")
    while(x != num):
        x = int(input())
        if(x < num):
            print("Your guess is too low.")
            cnt += 1
        elif(x > num):
            print ("Your guess is too high.")
            cnt += 1
        else: 
            txt = "Good job, {}! You guessed my number in {} guesses!"
            print (txt.format(name, cnt+1))
    
