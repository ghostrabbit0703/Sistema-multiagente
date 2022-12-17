import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="psicouni"
    )
    if mydb.is_connected():
        print("Conexion exitosa")
except Exception as ex:
    print (ex)

mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM psicouni.test")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
