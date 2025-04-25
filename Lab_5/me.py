import re
def find_gmail(a):
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', a)

txt = input("Enter your text: ")
print("Gmails: ",find_gmail(txt))