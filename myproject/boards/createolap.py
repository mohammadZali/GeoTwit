import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Zm1378@#$",
  database="citizen_base"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM boards_post")

myresult = mycursor.fetchall()

print(myresult)


