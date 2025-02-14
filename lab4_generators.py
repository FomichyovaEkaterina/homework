#Task1
N = int(input())
sqr = (i ** 2 for i in range(N + 1))
print(*sqr)

#Task2
N = int(input())
even = (str(i) for i in range(0, N + 1, 2))
print(",".join(even))

#Task3
N = int(input())
num = (i for i in range(N + 1) if i % 3 == 0 and i % 4 == 0)
print(*num)

#Task4
a, b = map(int, input().split())
squares = (i ** 2 for i in range(a, b + 1))
print(*squares)

#Task5
N = int(input())
down = (i for i in range(N, -1, -1))
print(*down)

