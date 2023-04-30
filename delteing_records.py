import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
cur=mydb.cursor()
myquery="DELETE FROM book WHERE title='Ajeet'"
cur.execute(myquery)
mydb.commit()