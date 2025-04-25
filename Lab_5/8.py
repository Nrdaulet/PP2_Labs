import re

def split_at_uppercase(s):
    return re.split(r"(?=[A-Z])", s)  

user_input = input("Enter a string: ")
print("Split result:", split_at_uppercase(user_input))
