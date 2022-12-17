from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ConnPSI import *
import matplotlib.pyplot as plt


class Grafica(Frame):
    def __init__(self, master,*args):
        super().__init__(master,*args)
        self.dbpsi = BasePsico()
        self.create_widgets()
        

    def create_widgets(self):
        self.fig, self.ax = plt.subplots(dpi=80,figsize=(7,5),facecolor='black')
        plt.title("Grafica",color='#00ff00',size=16, family="Arial")
        self.ax.axhline(linewidth=2,color='r')
        self.ax.axvline(linewidth=2,color='r')
        self.ax.set_xlabel("DECATIPOS", color='#00ff00')
        self.ax.set_ylabel("ESCALAS", color='#00ff00')
        self.ax.tick_params(direction='out',length=6, width=2,colors='#00ff00',grid_color='black',grid_alpha=1)
        
        self.frame1 = Frame(self.master,bg='red')
        self.frame1.grid(column=0,row=0,sticky='nsew')

        self.frame2 = Frame(self.master,bg='black')
        self.frame2.grid(column=1,row=0,sticky='nsew')

        self.frame3= Frame(self.master,bg='black')
        self.frame2.grid(column=2,row=0,sticky='nsew')

        self.canvas=FigureCanvasTkAgg(self.fig, master=self.frame3)
        self.canvas.get_tk_widget().pack(expand=True)

        self.canvas=FigureCanvasTkAgg(self.fig, master=self.frame1)
        self.canvas.get_tk_widget().pack(expand=True)
        Label(self.frame2, text='lectura',bg='green',fg='blue',font='verdana').pack(expand=True)
        Entry
        Button(self.frame2,text='obtenerdatos',bg='magenta',command=self.obtener_datos).pack(expand=True)
        Button(self.frame2,text='Graficar datos',bg='magenta',command=self.graficar_datos).pack(expand=True)
        
    def obtener_datos(self):
        
        self.sql=("SELECT escalas,dp FROM universitario_has_test INNER JOIN test on idtest=test_idtest where universitario_iduniversitario = 1")
        self.dbpsi.cursor.execute(self.sql)
        self.datos=self.dbpsi.cursor.fetchall()
    def graficar_datos(self):
        x=[]
        n=[]
        for i in self.datos:
            a= i[0]
            b= i[1]
            n.append(a)
            x.append(b)
            #print(a,b)
        self.ax.plot(n,x,color='b', linestyle='solid')
        self.canvas.draw()
        plt.grid(alpha=0.5)
        
       

if __name__ == "__main__":
    ventana=Tk()
    ventana.geometry('1000x600')
    ventana.resizable(0,0)
    ventana.config(bg='black')

    ventana.wm_title('Grafica')
    app = Grafica(ventana)
    app.mainloop()
print(__name__)
        



"""
def btn_clicked():
    print("Button Clicked")

window = Tk()

window.geometry("1000x700")
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

entry0_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//img_textBox0.png")
entry0_bg = canvas.create_image(
    325.5, 168.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry0.place(
    x=198, y=152,
    width=255,
    height=30)

entry1_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//img_textBox1.png")
entry1_bg = canvas.create_image(
    325.5, 256.0,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry1.place(
    x=198, y=240,
    width=255,
    height=30)

entry2_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//img_textBox2.png")
entry2_bg = canvas.create_image(
    325.5, 300.0,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry2.place(
    x=198, y=284,
    width=255,
    height=30)

entry3_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//img_textBox3.png")
entry3_bg = canvas.create_image(
    325.5, 212.0,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry3.place(
    x=198, y=196,
    width=255,
    height=30)

img0 = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=500, y=151,
    width=149,
    height=33)

entry4_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//img_textBox4.png")
entry4_bg = canvas.create_image(
    496.0, 496.5,
    image=entry4_img)

entry4 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry4.place(
    x=75, y=350,
    width=842,
    height=291)

img1 = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b1.place(
    x=500, y=198,
    width=149,
    height=34)

background_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA EVPSI//background.png")
background = canvas.create_image(
    605.5, 109.0,
    image=background_img)

marco = LabelFrame(window, text="agente evaluador psi")
marco.place(x=75, y=350,
            width=842,
            height=291)

Academicotv = ttk.Treeview(marco)
Academicotv.grid(column=0, row=2, columnspan=4)
Academicotv["columns"] = (
    "IDUNIVERSITARIO", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "NOMCARRERA", "NUMPREGUNTA", "AUTOCALIFICACION")
Academicotv.column("#0", width=0, stretch=NO)
Academicotv.column("IDUNIVERSITARIO", width=50, anchor=CENTER)
Academicotv.column("NOMBRE", width=100, anchor=CENTER)
Academicotv.column("APELLIDO PATERNO", width=150, anchor=CENTER)
Academicotv.column("APELLIDO MATERNO", width=150, anchor=CENTER)
Academicotv.column("NOMCARRERA", width=150, anchor=CENTER)
Academicotv.column("NUMPREGUNTA", width=150, anchor=CENTER)
Academicotv.column("AUTOCALIFICACION", width=100, anchor=CENTER)

Academicotv.heading("#0", text="")
Academicotv.heading("IDUNIVERSITARIO", text="IDUNIVERSITARIO", anchor=CENTER)
Academicotv.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
Academicotv.heading("APELLIDO PATERNO", text="APELLIDO PATERNO", anchor=CENTER)
Academicotv.heading("APELLIDO MATERNO", text="APELLIDO MATERNO", anchor=CENTER)
Academicotv.heading("NOMCARRERA", text="NOMCARRERA", anchor=CENTER)
Academicotv.heading("NUMPREGUNTA", text="NUMPREGUNTA", anchor=CENTER)
Academicotv.heading("AUTOCALIFICACION", text="AUTOCALIFICACION", anchor=CENTER)


def vaciar_tabla():
    filas = Academicotv.get_children()
    for fila in filas:
        Academicotv.delete(fila)
        
def llenar_tabla():
    vaciar_tabla()
    sql = "SELECT test_idtest,iduniversitario,nomuni,appatuni,apmatuni,nomcarrera,autocalificacion FROM universitario_has_test inner join universitario on idUniversitario = universitario_iduniversitario inner join carrera on carrera_idcarrera=idcarrera "
    #sql= "SELECT * FROM psicouni.universitario;"
    dbpsi.cursor.execute(sql)
    filas = dbpsi.cursor.fetchall()
    for fila in filas:
        id = fila[0]
        Academicotv.insert("",END,id, text=id,values=fila)

llenar_tabla()
window.resizable(False, False)
window.mainloop()

"""
