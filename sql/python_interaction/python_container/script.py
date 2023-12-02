import psycopg2
import random
import string

# establish connection with database
conn = psycopg2.connect(
    dbname = "docker_app_db",
    user = "docker_app",
    password = "docker_app",
    # interesting that host name match
    # with the container name
    # where database deployed
    host = "pg_example_posgres_cont"
)

# add 20 random values to the database
cur = conn.cursor()
for i in range(20):
    text = ''.join(random.choices(string.ascii_lowercase, k=20))
    query = f"INSERT INTO main_table (id, text) VALUES ('{i}', '{text}');"
    cur.execute(query)
cur.close()

print("Adding records is done!")

# commit changes and close the connection
conn.commit()
conn.close()