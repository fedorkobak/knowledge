import psycopg2

conn = psycopg2.connect(
    port = ""
    dbname = "docker_app_db",
    user = "docker_app",
    password = "docker_app",
    # host = "database"
)

conn.close()

print("hello world")