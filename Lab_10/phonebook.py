# import csv
# import psycopg2 

# conn = psycopg2.connect(
#     host = 'localhost',
#     dbname = "phonebook_db",
#     user = 'postgres',
#     password = '87654321'

# )

# cur = conn.cursor()
# print('Connected sucessfully.')
# with open(r'C:\Users\TUF Gaming\OneDrive\Рабочий стол\PP2\Lab_10\contacts.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     try:
#         next(reader)
#         for row in reader:
#             cur.execute(
#                 "INSERT INTO phonebook(name, phone) VALUES (%s, %s)",
#                 (row[0], row[1])
#         )
#         conn.commit()
#         print("Data loaded from CSV.")
#     except StopIteration:
#         print("No data found in CSV file")


# name = input("Enter name: ")
# phone = input("Enter phone: ")

# cur.execute(
#     "INSERT INTO phonebook(name, phone) VALUES(%s, %s)",
#     (name, phone)
# )

# conn.commit()
# print("Contact added!")


# cur.execute("SELECT * FROM phonebook")
# rows = cur.fetchall()

# for row in rows:
#     print(row)

# name = input("Enter name to update: ")
# new_phone = input("Enter new phone number: ")

# cur.execute(
#     "UPDATE phonebook SET phone = %s WHERE name = %s",
#     (new_phone, name)
# )

# conn.commit()
# print("Phone number updated. ")

# name = input("Enter name to delete: ")

# cur.execute(
#     "DELETE FROM phonebook WHERE name = %s",
#     (name,)
# )
# conn.commit()
# print("Contact deleted(if existed).")

# phone = input("Enter phone number to delete: ")

# cur.execute(
#     "DELETE FROM phonebook WHERE phone = %s",
#     (phone,)
# )
# conn.commit()
# print("Contact deleted(if existed).")

import csv
import psycopg2

def connect():
    conn = psycopg2.connect(
        host='localhost',
        dbname='phonebook_db',
        user='postgres',
        password='87654321'
    )
    return conn, conn.cursor()

def load_from_csv(cursor, conn, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute(
                "INSERT INTO phonebook(name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()
    print("Data loaded from CSV.")

def add_contact(cursor, conn):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute(
        "INSERT INTO phonebook(name, phone) VALUES(%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Contact added!")

def show_contacts(cursor):
    cursor.execute("SELECT * FROM phonebook")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_contact(cursor, conn):
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cursor.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (new_phone, name)
    )
    conn.commit()
    print("Phone number updated.")

def delete_contact_by_name(cursor, conn):
    name = input("Enter name to delete: ")
    cursor.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )
    conn.commit()
    print("Contact deleted (if existed).")

def delete_contact_by_phone(cursor, conn):
    phone = input("Enter phone number to delete: ")
    cursor.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )
    conn.commit()
    print("Contact deleted (if existed).")

def query_with_filter(cursor):
    print("Choose filter:")
    print("1 — Find by exact name")
    print("2 — Find by exact phone")
    print("3 — Find names starting with certain letters")
    choice = input("Your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        cursor.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    elif choice == '2':
        phone = input("Enter phone: ")
        cursor.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    elif choice == '3':
        start = input("Enter starting letters: ")
        cursor.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (start + '%',))
    else:
        print("Invalid choice.")
        return

    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results found.")

def main():
    conn, cursor = connect()
    print('Connected successfully.')

    # Можно загрузить CSV один раз при старте
    load_from_csv(cursor, conn, r'C:\Users\TUF Gaming\OneDrive\Рабочий стол\PP2\Lab_10\contacts.csv')

    # Основное меню
    while True:
        print("\nChoose an action:")
        print("1 — Add contact")
        print("2 — Show all contacts")
        print("3 — Update contact")
        print("4 — Delete by name")
        print("5 — Delete by phone")
        print("6 — Query with filters")
        print("0 — Exit")
        action = input("Your choice: ")

        if action == '1':
            add_contact(cursor, conn)
        elif action == '2':
            show_contacts(cursor)
        elif action == '3':
            update_contact(cursor, conn)
        elif action == '4':
            delete_contact_by_name(cursor, conn)
        elif action == '5':
            delete_contact_by_phone(cursor, conn)
        elif action == '6':
            query_with_filter(cursor)
        elif action == '0':
            break
        else:
            print("Invalid choice.")

    cursor.close()
    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
