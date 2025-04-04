import os

# Указываем путь (замени на свой)
path = r"C:\Users\TUF Gaming\OneDrive\Рабочий стол\python"

# Проверяем доступность
print("Path exists:", os.path.exists(path))
if os.path.exists(path):
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
