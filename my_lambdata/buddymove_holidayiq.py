import pandas as pd
from sqlalchemy import rgb_db.py

df = pd.read_csv('https://github.com/techthumb1/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/buddymove_holidayiq.csv')
df.to_sql('Buddy Move', con)