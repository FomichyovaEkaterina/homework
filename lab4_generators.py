#Task1
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2
N = int(input())
for square in square_generator(N):
    print(square, end=" ")

#Task2
def even_generator(N):
    for i in range(0, N + 1, 2):
        yield i
N = int(input())
print(",".join(map(str, even_generator(N))))

#Task3
def divisible(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = int(input())
print(list(divisible(N)))

#Task4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a, b = map(int, input().split())
for sq in squares(a, b):
    print(sq, end=" ")
print()

#Task5
def countdown(n):
    for i in range(n, -1, -1):
        yield i
N = int(input())
print(" ".join(map(str, countdown(N))))


