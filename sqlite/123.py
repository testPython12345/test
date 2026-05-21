import sqlite3

db = sqlite3.connect("example.db")

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_1(
               user_id INTEGER PRIMARY KEY
               ,name TEXT NOT NULL
               ,age INTEGER
               ,email TEXT
               )
            """)

cursor.execute("""
    INSERT INTO users_1(name, age, email)
    VALUES
    ('asdfa', 24, 'asdasd@mail.ru'),
    ('asdfa', 17, 'sfdf@mail.ru'),
    ('asdfa', 4, 'fsd@mail.ru'),
    ('asdfa', 14, 'fsdfsd@mail.ru'),
    ('asdfa', 34, 'fsdsfs@mail.ru')
""")
db.commit()

cursor.execute("""
    SELECT * FROM users_1
    WHERE age > 25
    ORDER BY age DESC
""")

cursor.execute("""SELECT * FROM users_1""")
users = cursor.fetchall()
for i in users:
    print(i)

db.close()




