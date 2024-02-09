# 1
class superstring:
    def getString(self):
        self.a = input()
    def printString(self):
        print (self.a.upper())
        

a = superstring()
# a.getString()
# a.printString()

# 2
class Shape:
    def area(self, s = 0):
        return (self.s)
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return (self.length**2)

a = Square(5)
# print(a.area())
    
# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    
a = Rectangle(5, 7)
# print(a.area())

# 4
import math 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print (self.x, self.y)
    def move(self):
        self.x = int(input())
        self.y = int(input())
        print ("Changed the coordinates!")
    def dist(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        return (math.sqrt((self.x1 - self.x)**2 + (self.y1 - self.y)**2))
    
a = Point(-1, 1)
# a.show()
# a.move()
# print (a.dist(5, 6))

# 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, sum):
        self.balance += sum
        print ("Balance changed:", self.balance)
    def withdraw(self, sum):
        if(sum > self.balance):
            print ("Not enough money to withdraw")
        else:
            self.balance -= sum
            print("Balance changed:", self.balance)
    
# idk = Account("James", 10000)
# idk.deposit(500)
# idk.withdraw(100000)

# 6
nums = [1, 3, 3, 5, 7, 6, 9]
def is_prime(a):
    for i in range(2, a):
        if(a%i == 0):
            return False
    return True

primes = list(filter(is_prime, nums))
print(primes)

