import os
def delete_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist!")
        return

    if not os.access(file_path, os.W_OK):
        print("No permission to delete the file!")
        return

    os.remove(file_path)
    print("File deleted successfully!")

file_path = r"C:\Users\TUF Gaming\OneDrive\Рабочий стол\python\Текстовый документ.txt"
delete_file(file_path)