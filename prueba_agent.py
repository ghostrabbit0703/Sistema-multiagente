import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="base_academico"
    )
    if mydb.is_connected():
        print("Conexion exitosa")
except Exception as ex:
    print (ex)

mycursor=mydb.cursor()
#mycursor.execute("SELECT * FROM base_academico.universitario_has_carrera_has_seccion Where Carrera_has_Asignatura_Asignatura_idAsignatura = 19 or Carrera_has_Asignatura_Asignatura_idAsignatura=20 or Carrera_has_Asignatura_Asignatura_idAsignatura=21 or Carrera_has_Asignatura_Asignatura_idAsignatura=22 or Carrera_has_Asignatura_Asignatura_idAsignatura=23 or Carrera_has_Asignatura_Asignatura_idAsignatura=24")
mycursor.execute("SELECT * FROM base_academico.universitario_has_carrera_has_seccion;")
#mycursor.execute("SELECT * from Information_Schema.Tables where table_type = 'base_academico';")
myresult=mycursor.fetchall()
Almacen=[]
alma={}
for x in myresult:
    if x[5]>75:
     Almacen.append(x)   
     print(x)
print ("este es el almacen")
print (Almacen)
Estudiante=mydb.cursor()
Estudiante.execute("SELECT * FROM base_academico.universitario;")
Estudianteresult=mycursor.fetchall()

for y in Estudianteresult:
    for x in myresult:
        if y[0] == x[0]:
            print("Estudiantes aprobados academiacamente",y[0],y[2])
