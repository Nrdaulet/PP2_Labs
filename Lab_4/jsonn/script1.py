import json

with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON    

print("Students and their average point:")
for student in data["students"]:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: {avg_grade:.2f}")
