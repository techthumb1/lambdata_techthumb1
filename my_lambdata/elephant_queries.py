#import psycopg2
import sqlite3

DB_NAME = "ijujqpth"
DB_USER = "ijujqpth"
DB_PASSWORD = "zO2olwovi1K9Z005-n0tvwyc0JNEp7U9"
DB_HOST = "hansken.db.elephantsql.com"

connection = sqlite3.connect(dbname=DB_NAME, user=DB_USER,
                              password=DB_PASSWORD, host=DB_HOST)

print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

cursor.execute('SELECT * from demo;')

result = cursor.fetchall()
for row in result:
    print(result)