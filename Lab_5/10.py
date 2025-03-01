import re

def camel_to_snake(camel_str):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()

# User input
user_input = input("Enter a CamelCase string: ")
print("snake_case:", camel_to_snake(user_input))
