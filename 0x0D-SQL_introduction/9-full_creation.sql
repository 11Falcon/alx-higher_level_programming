-- creates a table second_table in database and add multiples rows
CREATE TABLE IF NOT EXISTS second_table(id int, name VARCHAR(256), score int);
INSERT INTO second_table(id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Jane Smith", 30);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob Johnson", 22);
INSERT INTO second_table (id, name, score) VALUES (4, "Alice Williams", 28);
