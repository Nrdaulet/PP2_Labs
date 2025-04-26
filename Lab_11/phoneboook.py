import psycopg2

conn = psycopg2.connect(dbname="phonebook_db", user="postgres", password="87654321", host="localhost", port="5432")
cur = conn.cursor()

# 1. Поиск по шаблону
cur.execute("SELECT * FROM search_users(%s)", ("Ali",))
print("🔍 Поиск:", cur.fetchall())

# 2. Добавить или обновить одного
cur.execute("CALL insert_or_update_user(%s, %s)", ("Alice", "87001112233"))

# 3. Вставка списка пользователей
user_list = [["Alice", "abc"], ["Dave", "87778889999"], ["Eve", "123"]]
cur.execute("CALL insert_users(%s::text[][], NULL)", (user_list,))

# 4. Пагинация
cur.execute("SELECT * FROM get_users(%s, %s)", (5, 0))
print("📄 Первая страница:", cur.fetchall())

# 5. Удаление
cur.execute("CALL delete_user(%s)", ("Alice",))

conn.commit()
cur.close()
conn.close()
