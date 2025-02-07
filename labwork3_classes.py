#1
class StringManipulator:
    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())
sm = StringManipulator()
sm.getString()
sm.printString()

#2
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
square = Square(4)
print("Area of square:", square.area())

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rectangle = Rectangle(5, 3)
print("Area of rectangle:", rectangle.area())  # 15

#4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()
p2.show()
p1.move(3, 3)
p1.show()
distance = p1.dist(p2)
print(f"Distance between points: {distance}")

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
account = Account("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)

#6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 10, 15, 17, 20, 23]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)

