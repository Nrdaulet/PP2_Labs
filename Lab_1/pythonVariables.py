x = 5
y = "John"
print(type(x))
print(type(y))

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

a = 4
A = "Sally"
#A will not overwrite a

#Variable names
my_variable_name = "Nurdaulet"

#Assign Multiple Values
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Global Variables
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)