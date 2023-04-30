import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

cur=mydb.cursor()
s="SELECT * FROM book"
cur.execute(s)
result=cur.fetchall()
for rec in result:
    print (rec)