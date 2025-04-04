def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)

# Укажи путь к файлу
file_path = r"C:\Users\TUF Gaming\OneDrive\Рабочий стол\python\h.py"

# Выведем количество строк
print("Number of lines:", count_lines(file_path))
