import pyodbc

db_driver='{SQL Server}'
db_server = 'LAPTOP-OLVBJSU6'
db_database = 'MusicWorld'

conn = pyodbc.connect('Driver='+db_driver+';Server='+db_server+';Database='+db_database+';Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM MusicWorld.dbo.Users')

for row in cursor:
    print(row)