a = "Hello"
print(a)

#Slicing strings
b = "Hello, World!"
print(b[-5:-2])

#Modify strings
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concatenate strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Format strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Escape strings
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

#String methods
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case