import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
try:
    cursor.execute('create table user(id varchar(20) primary key, name varchar(200))')
    cursor.execute('insert into user(id, name) values(\'1\', \'jack\')   ')
    cursor.execute('select * from user')
    result = cursor.fetchall()
    print(result)
except BaseException as e:
    print(e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()