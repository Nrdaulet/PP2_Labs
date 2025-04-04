import os

# Указываем путь вручную
path = r"C:\Users\TUF Gaming\OneDrive\Рабочий стол\python"  # Замени на свой путь

# Проверяем, существует ли путь
if os.path.exists(path):
    # Список всех элементов в указанной папке
    all_items = os.listdir(path)

    # Разделяем файлы и папки
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    # Вывод результатов
    print("Directories:", directories)
    print("Files:", files)
    print("All items:", all_items)
else:
    print("Invalid path! Please enter a correct one.")
