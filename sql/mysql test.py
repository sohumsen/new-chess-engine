import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="Sohum", passwd="sohum567", database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
