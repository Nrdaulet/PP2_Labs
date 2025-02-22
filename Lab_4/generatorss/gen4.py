def square(a,b):
    for i in range(a, b+1):
        yield i*i
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(*square(a,b),sep=",")