CREATE TABLE simple_table(
    id TEXT NOT NULL,
    text TEXT NOT NULL
);
INSERT INTO simple_table (id, text) VALUES
(0, 'Text1'),
(1, 'tExT2'),
(3, 'TEXT3');

CREATE TABLE non_unique_values(
    col1 TEXT,
    col2 TEXT
);
INSERT INTO non_unique_values(col1, col2) VALUES
('A', 'X'),
('A', 'Y'),
('A', 'X'),
('B', 'X'),
('C', 'Y'),
('C', 'Y');


CREATE TABLE table_with_nulls(
    col1 TEXT,
    col2 INT
);
INSERT INTO table_with_nulls(col1, col2) VALUES
('A', NULL),
('A', 1),
('A', 2),
(NULL, 1),
('C', 3),
(NULL, 4);