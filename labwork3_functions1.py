#Python Function1
#Task 1
def x(grams):
    print("ounces=",28.3495231 * grams)
grams=int(input("grams= "))
x(grams)

#Task2
def q(F):
    print("C=",(5 / 9) * (F - 32) )
F=int(input("Fahrenheit= "))
q(F)

#Task3
def solve(numheads, numlegs):
    R = int((numlegs / 2) - numheads)
    C = int(numheads - R)
    print(f"Chickens: {C}, Rabbits: {R}")
heads=35
legs=94
solve(heads,legs)

#Task4
def filter_prime(numbers):
    primes=[]
    for i in numbers:
        i=int(i)
        if i <= 1:
            continue
        if i==2 or i==3:
            primes.append(i)
        for j in range(2, int(i ** 0.5) + 1):
            if i % j != 0:
                primes.append(i)
    return primes
numbers = input("Enter elements separated by spaces: ").split()
print(filter_prime(numbers))

#Task5
def permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        permutations(remaining, prefix + s[i])
user_input = input("Enter a string: ")
permutations(user_input)

#Task6
def reverse(str):
    str_rev=[]
    for i in range(1,len(str) + 1):
        str_rev.append(str[-i])
    print(*str_rev)
str = input("Enter string: ").split()
reverse(str)

#Task7
def has_33(nums):
    for i in range(len(nums)):
        if nums[i]=="3":
            if nums[i+1]=="3":
                return True
nums = input("Enter elements separated by spaces: ").split()
print(has_33(nums))

#Task9
import math
def volume(radius):
    print("Volume=",(4.0 / 3) * math.pi * radius ** 3)
radius=int(input("Enter the radius: "))
volume(radius)

#Task10
def unique(list):
    q_list=[]
    count=0
    for i in list:
        for j in range(len(list)):
            if i==list[j]:
                count+=1
        if count==1:
            q_list.append(i)
        count=0
    print(*q_list)
list = input("Enter elements separated by spaces: ").split()
unique(list)

#Task11
def palindrome(s):
    s = ''.join(s.split()).lower()
    return s == s[::-1]
input_str = input("Enter a word or phrase: ")
if palindrome(input_str):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#Task12
def histogram(list2):
    for i in list2:
        i=int(i)
        print("*"*i)
list2 = input("Enter elements separated by spaces: ").split()
histogram(list2)

#Task13
import random
right_num=random.randint(1,20)
guesses=1
name=input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
numb=int(input("Take a guess\n"))
while True:
    if numb==right_num:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
        break
    elif numb < right_num:
        print("Your guess is too low.")
        numb=int(input("Take a guess.\n"))
        guesses+=1
    else:
        print("Your guess is too high.")
        numb = int(input("Take a guess.\n"))
        guesses+=1

