import re

def match_pattern(string):
    pattern = r"^[A-Z][a-z]+$" 
    if re.fullmatch(pattern, string):
        return "Match found!"
    return "No match."

# User input
user_input = input("Enter a string: ")
print(match_pattern(user_input))
