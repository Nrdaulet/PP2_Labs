import json

# Открываем JSON-файл и загружаем данные
with open("sample-data.json") as file:
    data = json.load(file)

# Вывод заголовков таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Speed':<10} {'MTU':<6}")
print("-" * 80)

# Обрабатываем данные и выводим их в виде таблицы
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {speed:<10} {mtu:<6}")
