import sqlite3
from sqlite3.dbapi2 import Error
import random
import functools


try:
    conn = sqlite3.connect('data.db')
    print("Succesfull")

except Error as e:
    print(e)
conn = conn.cursor()

rows = conn.fetchall()
maxRows = conn.execute("SELECT COUNT(*) FROM Accounts").fetchone()
mRoInt = functools.reduce(lambda sub, ele: sub * 10 + ele, maxRows)




class request:
   ranID = random.randint(0, mRoInt)
   print(rows[ranID])
    
print(request.ranID)
conn.close()