#Python Booleans
print(3.14 == 3.14)
print(10 != 9)
print(10 < 9)

a = 200
b = -33
if a*b > 0:
  print("b multiplied a is positive")
else:
  print("b multiplied a is negative")

print(bool("KBTU"))
print(bool(123))
print(bool({1:"apple", 2:"cherry", 3:"banana"}))

def myFunction() :
  return False
if myFunction():
  print("its true")
else:
  print("its false")


#Python Operators
print((100 + 5 * 3)**5)


#Python Lists
list1 = ["abc", 34, True, 47.324, "male"]
thislist = ["apple", "banana", "cherry"]
print(list1[-4:-1])
list1.insert(1, "orange")
list1.extend(thislist)
list1.clear()

numbers = [23, 55, 10, 20, 15]
newlist = [x for x in numbers if x%2==0]
newlist.reverse()
mylist = newlist[:]
mylist.extend(numbers)
print(newlist)


#Python Tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[2:])
y = list(thistuple)
y[1] = "kiwi"
x = tuple(y)
print(x)
mytuple = x * 2
print(mytuple)


#Python Sets
thisset = {"pen", "book", "copybook", "paper"}
print("pencil" not in thisset)
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


#Python Dictionaries
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
car.update({"color": "red"})
car.pop("model")
print(car)


#Python If ... Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# or short hand if
if a > b: print("a is greater than b")


#Python While Loops
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

age = [15, 14, 19]
name = ["Mike", "Kate", "John"]
for x in age:
  for y in name:
    print(x, y)
