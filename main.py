import sqlite3
import pandas

# establish connection to database
con = sqlite3.connect('database.db')

# create cursor object that looks at the rows and gives you data
cur = con.cursor()

# run SQL query & print the results
# this one is to get all rows and all columns by order
df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)

# df.to_csv('database.csv', index=None)
df.to_excel('database.xlsx', index=None)