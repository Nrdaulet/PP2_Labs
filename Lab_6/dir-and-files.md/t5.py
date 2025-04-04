def write_list_to_file(file_path, data):
    with open(file_path,'w', encoding='utf-8')as file:
        for item in data:
            file.write(str(item)+ '\n')

my_list = ["Apple", 'Banana','Cherry', 'Orange']

file_path = r"C:\Users\TUF Gaming\OneDrive\Рабочий стол\python\data\text.txt"
write_list_to_file(file_path, my_list)