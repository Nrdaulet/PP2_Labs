def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i 

n = int(input("Enter a number: "))
print(*even_numbers(n),sep=",")

