CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL
);

INSERT INTO student (name,email,dob,phone,marks)
VALUES ('tabitha','tabitha@gmail.com','2007-07-5',254113963,88.2);

SELECT * FROM student


