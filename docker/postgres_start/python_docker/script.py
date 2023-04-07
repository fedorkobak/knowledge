import psycopg2
import random
import string

# устанавливаю соединение с базой
conn = psycopg2.connect(
    dbname = "docker_app_db",
    user = "docker_app",
    password = "docker_app",
    host = "database"
)

# вставляем в базу 20 случайных записей
cur = conn.cursor()
for i in range(20):
    text = ''.join(random.choices(string.ascii_lowercase, k=20))
    query = f"INSERT INTO main_table (id, text) VALUES ('{i}', '{text}');"
    cur.execute(query)
cur.close()

# отсылаем зименения и закрываем соединение
conn.commit()
conn.close()