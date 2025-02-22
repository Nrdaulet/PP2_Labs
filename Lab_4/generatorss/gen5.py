def down(n):
    for i in range(n, -1,-1):
        yield i

n = int(input("Enter a number: "))
print(*down(n),sep=",")