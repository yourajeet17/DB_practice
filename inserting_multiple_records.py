import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test")
# print(mydb.connection_id)  #print connection id for showing success connection
cur=mydb.cursor()
s="INSERT INTO book(bookid, title, price) VALUES (%s,%s,%s)"
b=[(6,'Hello',400),(7,'sumitra',700),(8,'ncert',800)]
cur.executemany(s,b)
mydb.commit()
print("Multiple records are inserted successfully")
