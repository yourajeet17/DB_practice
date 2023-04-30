import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
cur=mydb.cursor()
myquery="UPDATE book SET price=price+10 where price<500"
cur.execute(myquery)
mydb.commit()