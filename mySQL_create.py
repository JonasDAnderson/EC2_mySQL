import  mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="",
    passwd="",
    database=""
)

mycursor = mydb.cursor()

#mycursor.execute("SHOW TABLES")
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#mycursor.execute("CREATE TABLE customers2 (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("Michelle", "Blue Village")
#mycursor.execute(sql, val)


#mydb.commit()

#print(mycursor.rowcount, "was inserted.")
#print("1 record inserted, ID:", mycursor.lastrowid)