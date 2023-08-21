CREATE TABLE main_table(
    sepallength REAL,
    sepalwidth REAL,
    petallength REAL,
    petalwidth REAL,
    class VARCHAR(20)
);

COPY main_table(sepallength, sepalwidth, petallength, petalwidth,class)
FROM '/iris_csv.csv'
DELIMITER ','
CSV HEADER;