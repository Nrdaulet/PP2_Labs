import os

# Указываем путь (замени на свой)
path = r"C:\Users\TUF Gaming\OneDrive\Рабочий стол\python"

# Проверяем, существует ли путь
if os.path.exists(path):
    print("Path exists:", True)
    print("Directory:", os.path.dirname(path))  # Папка, в которой находится файл
    print("Filename:", os.path.basename(path))  # Имя файла
else:
    print("Path exists:", False)
