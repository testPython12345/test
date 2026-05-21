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

SELECT DEPARTMENT_ID FROM employees
EXCEPT
SELECT DEPARTMENT_ID FROM departments;

SELECT username, age  FROM users_2;



CREATE TABLE rabotniki(
    id INTEGER PRIMARY KEY
    ,full_name TEXT
    ,department TEXT
    ,salary INTEGER
);
INSERT INTO rabotniki(full_name, department, salary)
VALUES
    ('Daniil', 'IT', 1000000),
    ('PEter', 'Marketing', 25000),
    ('Olga', 'Manage', 50000),
    ('Maria', 'IT', 100000),
    ('Ivan', 'Marketing', 67000),
    ('Dmitri', 'Manage', 95000);

SELECT * FROM rabotniki;


SELECT full_name, salary FROM rabotniki
WHERE salary > (SELECT AVG(salary) FROM rabotniki);



SELECT full_name, salary FROM rabotniki
GROUP BY salary
HAVING salary > 50000
ORDER BY salary DESC;


SELECT * FROM sales;


УРОВЕНЬ 1: 
    1) Вывести все заказы
    2) Вывести только продукты и их цену
    3) Найти все заказы из Asia
    4) Найти все товары категории Electronics
УРОВНЬ 2: 
    1) Вывести все заказы где стоимость заказы выше 300
    2) Вывести заказ где количество товара больше 2
    3) Вывести заказы с оплатой PayPal
    4) Отсортировать товары по их цене
    5) Вывести 5 самых дорогих товаров
УРОВЕНЬ 3: 
    1) Найти среднюю цену заказов
    2) Посчитать сколько заказов в каждом регионе
    3) Найти среднюю сумму заказов для каждого региона
    4) Вывести все уникальные товары (Product_Name = sales.Product_Name)
SELECT Product_Name, Region FROM sales
WHERE Region = 'Asia';
SELECT Product_Name, (Unit_Price*Units_Sold) FROM sales
WHERE (Unit_Price*Units_Sold) > 300;
SELECT ROUND(AVG(Unit_Price*Units_Sold),2) AS 'СР' FROM sales;

WITH Product_counts AS (
    SELECT Product_Name, COUNT(*) AS total 
    FROM sales
    GROUP BY Product_Name
)
SELECT Product_Name
FROM Product_counts
WHERE total >1;
*/

SELECT * FROM sqlite_master;