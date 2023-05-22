# запуск контейнера
docker run --rm -d\
    --name database\
    -e POSTGRES_USER=docker_app\
    -e POSTGRES_PASSWORD=docker_app\
    -e POSTGRES_DB=docker_app_db\
    custom_postgres

docker-compose --wait

# запуск скрипта создающего таблицу
docker exec database \
    psql --username docker_app --dbname docker_app_db -f create_table.sql

# для того, чтобы провалиться в базу данных следует использовать команду
# docker exec -it database psql --username docker_app --dbname docker_app_db
# выйти из базы данных \q