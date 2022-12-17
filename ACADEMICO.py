from tkinter import *
from tkinter import ttk
from ConnAcademico import *
from ConnAntecedentes import *
from ConnVidaUni import *
from ConnPSI import *
dbpsi=BasePsico()
db=BaseAcademico()
dbant= BaseAntecedentes()
dbvidauni=Basevidauni()
"""
class ACADEMICO(Frame):
    

    def __init__(self, master=None):
        super().__init__(master, width=1000, height=9000)
        self.master = master
        self.pack()
        self.create_widgedts_AB()
        self.btn_clicked()

    def btn_clicked(self):
        print("Button Clicked")

    def create_widgedts_AB(self):
        self.canvas = Canvas(self, bg="#ffffff", height=700, width=1000,bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA ACADEMICO//background1.png")
        self.background = self.canvas.create_image(433.5, 514.0,image=self.background_img)
        self.canvas.create_text(500.0, 76.0,text="ACADEMICO",fill="#000000",font=("None", int(30.0)))
        self.img0 = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA ACADEMICO//img01.png")
        self.b0 = Button(image=self.img0,borderwidth=0,highlightthickness=0,command=self.btn_clicked,relief="flat")
        self.b0.place(x=401, y=600,width=249,height=55)
 
"""
def btn_clicked():
    consulta_vidauni()
    
def btn_clicked1_antecedentes():
    consulta_antecedentes()

def btn_clicked2_PSI():
    consulta_PPSI()
window = Tk()
window.geometry("1000x900")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=700,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA ACADEMICO//background1.png")
background = canvas.create_image(
    433.5, 514.0,
    image=background_img)

canvas.create_text(
    500.0, 76.0,
    text="ACADEMICO",
    fill="#000000",
    font=("None", int(30.0)))

img0 = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA ACADEMICO//img01.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=301, y=600,
    width=249,
    height=55)

img02 = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA ACADEMICO//img02.png")
b1 = Button(
    image=img02,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked1_antecedentes,
    relief="flat")

b1.place(
    x=301, y=670,
    width=249,
    height=55)

img03 = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA ACADEMICO//img03.png")
b2 = Button(
    image=img03,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked2_PSI,
    relief="flat")

b2.place(
    x=650, y=600,
    width=249,
    height=55)



marco = LabelFrame(window, text="Agente Academico")
marco.place(x=150,y=150,width=700,height=450)
#
#
Academicotv = ttk.Treeview(marco)
Academicotv.grid(column=0, row=2, columnspan=4)
Academicotv["columns"] = (
    "RU","CI", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO","NOTA")
Academicotv.column("#0", width=0, stretch=NO)
Academicotv.column("RU", width=50, anchor=CENTER)
Academicotv.column("CI", width=50, anchor=CENTER)
Academicotv.column("NOMBRE", width=100, anchor=CENTER)
Academicotv.column("APELLIDO PATERNO", width=150, anchor=CENTER)
Academicotv.column("APELLIDO MATERNO", width=150, anchor=CENTER)
Academicotv.column("NOTA", width=150, anchor=CENTER)

Academicotv.heading("#0", text="")
Academicotv.heading("RU", text="RU", anchor=CENTER)
Academicotv.heading("CI", text="CI", anchor=CENTER)
Academicotv.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
Academicotv.heading("APELLIDO PATERNO", text="APELLIDO PATERNO", anchor=CENTER)
Academicotv.heading("APELLIDO MATERNO", text="APELLIDO MATERNO", anchor=CENTER)
Academicotv.heading("NOTA", text="NOTA", anchor=CENTER)


def vaciar_tabla():
    filas=Academicotv.get_children()
    for fila in filas:
        Academicotv.delete(fila)
##

def llenar_tabla():
    vaciar_tabla()
    sql="SELECT iduniversitario,CI_Uni,NomUniversitario,ApellidoPaterno,ApellidoMaterno, avg(nota)FROM (universitario as u inner join universitario_has_carrera_has_seccion as usc on u.idUniversitario = usc.Universitario_has_Carrera_Universitario_idUniversitario inner join asignatura as a on a.idAsignatura = Carrera_has_Asignatura_Asignatura_idAsignatura)"
    db.cursor.execute(sql)
    filas=db.cursor.fetchall()
    for fila in filas:
        id=fila[0]
        Academicotv.insert("",END,id, text=id,values=fila)
##

def consulta_antecedentes():
    vaciar_tabla()
    #sql = "SELECT iduniversitario,nomuni,appatuni,apmatuni,nomcarrera,test_idtest,autocalificacion FROM universitario_has_test inner join universitario on idUniversitario = universitario_iduniversitario inner join carrera on carrera_idcarrera=idcarrera;"
    sql="SELECT idUniversitario,nomuni,patuni,matuni,idantecedentes,tipo FROM (universitario_has_antecedentes join universitario on idUniversitario=Universitario_idUniversitario join antecedentes on idantecedentes=antecedentes_idantecedentes)"
    dbant.cursor.execute(sql)
    filas=dbant.cursor.fetchall()
    for fila in filas:
        id=fila[0]
        Academicotv.insert("",END,id, text=id,values=fila)
#def btn_clicked():
def consulta_vidauni():
    vaciar_tabla()
    sql="SELECT iduniversitario, Nombre,`apellido pat`,`apellido mat`,universitario_has_actividadescol,tipo,detalle FROM universitario_has_actividades inner join actividades on id_actividad = actividades_id_actividad inner join universitario on Universitario_iduniversitario = idUniversitario;"
    dbvidauni.cursor.execute(sql)
    filas=dbvidauni.cursor.fetchall()
    for fila in filas:
        id=fila[0]
        Academicotv.insert("",END,id, text=id,values=fila)
def consulta_PPSI():
    vaciar_tabla()
    sql="SELECT * FROM psicouni.universitario_has_test;"
    dbpsi.cursor.execute(sql)   
    filas=dbpsi.cursor.fetchall()
    for fila in filas:
        id=fila[0]
        Academicotv.insert("",END,id, text=id,values=fila)
llenar_tabla()
window.resizable(False, False)
window.mainloop()
print(__name__)