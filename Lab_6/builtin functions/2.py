def count_case(st):
    upper_count = sum(1 for i in st if i.isupper())
    lower_count = sum(1 for i in st if i.islower())

    print("Uppercase letters: ", upper_count)
    print("Lowercase letters: ", lower_count)

text = input("Enter a string: ")
count_case(text)

