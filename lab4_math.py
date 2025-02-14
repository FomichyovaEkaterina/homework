import math
#Task1
degree = int(input())
x = math.pi
print("Radian:", degree * (x/180))

#Task2
height = int(input())
first = int(input())
second = int(input())
print("Area:", height/2 * (first + second))

#Task3
#Area = (a x p)/2
#apothem = a / (2 * tan((180 / n) *3.14159 / 180))
size = int(input())
length = int(input())
apothem = length / (2 * math.tan((180 / size) * math.pi /180))
perimetr = size * length
print("Area:", (apothem * perimetr) // 2)

#Task4
length_of_base = int(input())
height_of_parallelogram = int(input())
print("Area:", length_of_base * height_of_parallelogram)