import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()
# cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user2(id, name) values(\'2\', \'jack\')')
# cursor.execute(r'select * from user')

print(cursor.rowcount)

cursor.close()
conn.close()