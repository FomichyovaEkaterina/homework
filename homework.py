print("i am KBTU student")
if 5-3==2:
    print("Five minus three equals two!")
#print("heloooo")
x = 5
y = "John"
days = ["Monday", "Wednesday", "Sunday"]
x, y, z = days
print(x)
print(y)
print(z)
print(x + y + z)

x = "awesome"
def myfunc():
  x = "fantastic"
  print("My friend is " + x)

myfunc()

print("My friend is " + x)

x = 5.548
print(type(x))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)
b = int(y)
c = complex(x)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 100))

x = float(12)     # x will be 12.0
y = float(5.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("5.5") # w will be 4.2

for x in "Happy New year!":
  print(x)
a="Congratulations"
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")