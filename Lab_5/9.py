import re

def add_spaces(text):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

user_input = input("Enter a string: ")
print("Result:", add_spaces(user_input))
