import string

# Генерируем файлы от A.txt до Z.txt
for letter in string.ascii_uppercase:  # 'A' до 'Z'
    file_name = f"{letter}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"This is file {file_name}\n")

print("26 text files created successfully!")
