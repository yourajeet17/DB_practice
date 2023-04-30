import mysql.connector
import cgi
con = mysql.connector.connect(host="localhost", user="root",password="",database="test")

form=cgi.FieldStorage()
id=form.getvalue("id")
username=form.getvalue("username")
email=form.getvalue("email")



cur=con.cursor()
cur.execute("insert into test_tbl values(%s,%s,%s)",(id,username,email))
con.commit()
cur.close()
con.close()
print("Record Inserted successfully")