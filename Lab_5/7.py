import re

def snake_to_camel(snake_str):
    words = snake_str.split('_')  
    return words[0] + ''.join(word.capitalize() for word in words[1:])  

# User input
user_input = input("Enter a snake_case string: ")
print("CamelCase:", snake_to_camel(user_input))
