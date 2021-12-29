import mysql.connector
mydb = mysql.connector.connect(
    hosy='localhost',
    user='root',
    passwd='2004',
)
my_cursor = mydb.cursor()

my_cursor.execute('CREATE DATABASE database')
my_cursor.execute('SHOW DATABASES')
for db in my_cursor:
    print(db)