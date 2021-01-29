from psycopg2.extras import DictCursor
from dotenv import load_dotenv
import os

load_dotenv() # reads the content of the dotenv file and adds them to the enviro

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                              password=DB_PASSWORD, host=DB_HOST)

print("CONNECTION", type(connection))

# Here we will use an alternative method to be more explicit
# and include the column names.
cursor = connection.cursor(cursor_factory=DictCursor)
print("CURSOR", type(cursor))


cursor.execute('SELECT * from test_table;')
#print(type(result)) #> <class 'tuple'>
#result = cursor.fetchone()
#> (1, 'A row name', None)

result = cursor.fetchall()
for row in result:
    print('------')
    print(type(row))
    print(row)