import pymssql

conn = pymssql.connect(server="jamescarter2001.database.windows.net", user="dts", password="DigitalTechnology2022!", database="NymptonFoodHub")
cursor = conn.cursor()

cursor.execute("SELECT * from Customer")
row = cursor.fetchone()

conn.close()

print(row)