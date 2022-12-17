import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="universitariosantecedentes"
    )
    if mydb.is_connected():
        print("Conexion exitosa")
except Exception as ex:
    print (ex)
mycursor=mydb.cursor()
#mycursor.execute("SELECT * FROM base_academico.universitario_has_carrera_has_seccion Where Carrera_has_Asignatura_Asignatura_idAsignatura = 19 or Carrera_has_Asignatura_Asignatura_idAsignatura=20 or Carrera_has_Asignatura_Asignatura_idAsignatura=21 or Carrera_has_Asignatura_Asignatura_idAsignatura=22 or Carrera_has_Asignatura_Asignatura_idAsignatura=23 or Carrera_has_Asignatura_Asignatura_idAsignatura=24")
mycursor.execute("SELECT * FROM universitariosantecedentes.universitario_has_antecedentes as ua inner join universitario as u on Universitario_idUniversitario=idUniversitario;")
myresult=mycursor.fetchall()
almacen=[]
for x in myresult:
    if x[2]==2:
        print("el universitario",x[4],x[5],x[6],"no tiene procesos")
    else:
        
        print ("el universitario",x[4],x[5],x[6]," tiene procesos")
        
for x in myresult:
    if x[2]==1:
        almacen.append(x)
print('\n'.join(map(str, almacen)))
