






import sqlite3


connection = sqlite3.connect("database.db")
cursor = connection.cursor()



##################################3333

cursor.execute('''
               
CREATE table if not exists user(
    id INTEGER NOT NULL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL           
               )       
     ''')


users = [
    (1, "Bahtiyorjon", "Tolipov", 19),
    (2, "Hakimjon", "Qodirov", 23)
]


cursor.executemany('''

INSERT or REPLACE into user(id, first_name, last_name, age)               
VALUES (?, ?, ?, ?)
''', users)


cursor.execute("SELECT first_name FROM user WHERE age > 18")
users = cursor.fetchall()

for user in users:
    print(user[0])







connection.commit()
connection.close()
