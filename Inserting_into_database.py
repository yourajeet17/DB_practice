import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test")
# print(mydb.connection_id)  #print connection id for showing success connection
cur=mydb.cursor()
val1=input("Enter the id of the book\n")
val2=input("Enter the title of the book\n")
val3=input("Enter the price of the book\n")
s="INSERT INTO `book`(`bookid`, `title`, `price`) VALUES (%s,%s,%s)"
b=(val1,val2,val3)
cur.execute(s,b)
mydb.commit()
print("One record is inserted successfully")






#form=cgi.FieldStorage()
# id=form.getvalue("id")
# username=form.getvalue("username")
# email=form.getvalue("email")



# cur=con.cursor()
# cur.execute("insert into test_tbl values(%s,%s,%s)",(id,username,email))
# con.commit()
# cur.close()
# con.close()
# print("Record Inserted successfully")