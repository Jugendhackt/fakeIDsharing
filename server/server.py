import sqlite3

try:
    conn = sqlite3.connect('data.db')
    print("Succesfull")

except Error as e:
    print(e)

conn = conn.cursor()
conn.execute("SELECT * FROM Accounts")

rows = conn.fetchall()
print(rows)

conn.close()



