/*
CREATE TABLE users(
    id INTEGER PRIMARY KEY
    ,username VARCHAR(50)
    ,age INTEGER
    ,email TEXT
);
*/
/*
INSERT INTO users(username, age, email)
VALUES("ADSFDS", 0, 'DSFSD');

SELECT username, email FROM users;


CREATE TABLE users_1(
    id INTEGER PRIMARY KEY
    ,username VARCHAR(50) NOT NULL
    ,age INTEGER CHECK(age >= 0)
    ,email TEXT UNIQUE NOT NULL
);


INSERT INTO users_1(username, age, email)
VALUES
('Daniil', 0, '1234@mail.ru'),
('Peter', 25, 'peter123@gmail.com'),
('Ivan', 40, 'ivan@yandex.ru'),
('Roza', 20, 'roza@bk.com');




UPDATE users_1
SET age = 26
WHERE username = 'Peter';


UPDATE users_1
SET age = age + 1;


DELETE FROM users_1
WHERE id = 5;


DELETE FROM users;

DROP TABLE users;


CREATE TABLE users_2(
    id INTEGER PRIMARY KEY
    ,username VARCHAR(50) NOT NULL
    ,age INTEGER CHECK(age >= 0)
    ,email TEXT UNIQUE NOT NULL
);



INSERT INTO users_2(username, age, email)
SELECT username, age, email FROM users_1;




UPDATE users_2
SET username = 'TOP', 
    email = 'top@top.top',
    age = 0
WHERE id = 1;

SELECT * FROM users_2;


SELECT * 
FROM sqlite_master
WHERE type = 'table';


CREATE TABLE employees(
    ID INTEGER PRIMARY KEY
    ,FULL_NAME TEXT NOT NULL
    ,DEPARTMENT_ID INTEGER
);


CREATE TABLE departments(
    DEPARTMENT_ID INTEGER PRIMARY KEY
    ,DEPARTMENT_NAME TEXT NOT NULL
);


INSERT INTO employees(FULL_NAME, DEPARTMENT_ID)
VALUES
    ('Daniil', 1),
    ('Peter', 2),
    ('Ivan', 2);

INSERT INTO departments(DEPARTMENT_NAME)
VALUES
    ('IT'),
    ('Marketing'),
    ('1C');

SELECT * FROM employees;
SELECT * FROM departments;


SELECT employees.FULL_NAME, departments.DEPARTMENT_NAME
FROM employees
INNER JOIN departments ON 
    employees.DEPARTMENT_ID = departments.DEPARTMENT_ID;


INSERT INTO employees(FULL_NAME, DEPARTMENT_ID)
VALUES
    ('LEXA', 10);
    
SELECT employees.FULL_NAME, departments.DEPARTMENT_NAME
FROM employees
LEFT JOIN departments ON 
    employees.DEPARTMENT_ID = departments.DEPARTMENT_ID;


SELECT employees.FULL_NAME, departments.DEPARTMENT_NAME
FROM  departments
FULL JOIN employees ON 
    employees.DEPARTMENT_ID = departments.DEPARTMENT_ID;


SELECT FULL_NAME FROM employees
UNION
SELECT DEPARTMENT_NAME FROM departments;

SELECT FULL_NAME AS 'ФИО' FROM employees;

SELECT FULL_NAME FROM employees
EXCEPT
SELECT DEPARTMENT_NAME FROM departments;
*/
SELECT DEPARTMENT_ID FROM employees
EXCEPT
SELECT DEPARTMENT_ID FROM departments;