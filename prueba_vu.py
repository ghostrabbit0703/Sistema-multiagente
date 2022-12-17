from pickle import TRUE
from unittest import result
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="vidauni"
    )
    if mydb.is_connected():
        print("Conexion exitosa")
except Exception as ex:
    print (ex)

mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM vidauni.universitario_has_actividades")
myresult=mycursor.fetchall()
for x in myresult:
        print(x)
univid=mydb.cursor()
univid.execute("SELECT * FROM psicouni.universitario;")
unividresult=mycursor.fetchall()
for x in myresult:
    for y in unividresult:
        if y[0]==x[0]:
            print("El/LA Universitari@",y[1],y[2],y[3],"es aprobado por actividad universitaria")


