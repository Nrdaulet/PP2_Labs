import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = 'phonebook_db',
    user = 'postgres',
    password = "87654321"
)
cur = conn.cursor()

username = input("Enter your username: ")

cur.execute("SELECT id, username FROM users  WHERE username = %s",(username,))
user = cur.fetchone()

if user:
    user_id = user[0]
    cur.execute("SELECT score,level FROM user_score WHERE user_id = %s,"(user_id,))
    user_score = cur.fetchone()
    print(f"Welcome back, {username}! Your current level is {user_score[1]} with score {user_score[0]}")
else:
    # Если пользователя нет, создаем нового
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, 0, 1)", (user_id,))
    conn.commit()
    print(f"Welcome, {username}! You have been registered. Starting from level 1.")

# Закрываем соединение с базой данных
cur.close()
conn.close()