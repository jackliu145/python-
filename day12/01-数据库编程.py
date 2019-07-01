import sqlite3

sql_str = r'insert into user values(0, "jack")'

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user(id int primary key , name varchar(20))')
cursor.execute(sql_str)
cursor.execute(r'select * from user')
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()
