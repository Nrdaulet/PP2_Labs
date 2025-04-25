import re

def replace_chars(text):
    pattern = r"[ ,.]+"  # Match spaces, commas, or dots
    return re.sub(pattern, ":", text)

user_input = input("Enter a string: ")
print(replace_chars(user_input))
