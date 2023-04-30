#!C:\Users\ASUS\AppData\Local\Programs\Python\Python311
print("content-Type:text/html")
print()
import cgi

print("<h1>Welcome to Python<?h1>")
print("<hr/>")
print("<h1>Using input tag</h1>")
print("<body bgcolor='red'")

form=cgi.FieldStorage()
id=form.getvalue("id")
username=form.getvalue("username")
email=form.getvalue("email")

import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',password='',database="test")
cur=con.cursor()

cur.execute("insert into test_tbl values(%s,%s,%s)",(id,username,email))
con.commit()
cur.close()
con.close()
print("<h3>Record Inserted successfully</h3>")