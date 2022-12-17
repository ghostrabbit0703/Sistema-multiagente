from tkinter import * 
from tkinter import messagebox
#from ACADEMICO import *
from ConnAcademico import *
class LOGIN(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=1000,height=600)
        self.master= master
        self.pack()
        self.create_widgets()
        self.btn_clicked()
    #def validar(self):
      #  if self.entry1.get()=="Rummy":
       #     abrirAB(self)
        #else:
         #   messagebox.showwarning("Cuidado","Contraseña incorrecta")
    
    def create_widgets(self):
        self.canvas = Canvas(self,bg="#ffffff",height=600,width=1000,bd=0,highlightthickness=0,relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//background.png")
        self.background =self.canvas.create_image(427.0, 356.0, image=self.background_img)
        self.entry0_img = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(806.0, 239.5, image=self.entry0_img)
        self.entry0 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.entry0.place(x=688.0, y=210, width=236.0, height=57)
        self.entry1_img = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(809.0, 390.0, image=self.entry1_img)
        self.entry1 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.entry1.place(x=694.0, y=359, width=230.0, height=60)
        self.img0 = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//img0.png")
        self.b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0,command=self.btn_clicked, relief="flat")
        self.b0.place(x=717, y=489, width=181, height=41)
    def btn_clicked(self):
        print("")
        
        

"""class ACADEMICO(Frame):
    db = BaseAcademico()

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
        self.background_img = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA ACADEMICO//background1.png")
        self.background = self.canvas.create_image(433.5, 514.0,image=self.background_img)
        self.canvas.create_text(500.0, 76.0,text="ACADEMICO",fill="#000000",font=("None", int(30.0)))
        self.img0 = PhotoImage(file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA ACADEMICO//img01.png")
        self.b0 = Button(image=self.img0,borderwidth=0,highlightthickness=0,command=self.btn_clicked,relief="flat")
        self.b0.place(x=401, y=600,width=249,height=55)

"""
"""
window = Tk()

window.geometry("1000x600")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//background.png")
background = canvas.create_image(
    427.0, 356.0,
    image=background_img)

entry0_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//img_textBox0.png")
entry0_bg = canvas.create_image(
    806.0, 239.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry0.place(
    x=688.0, y=210,
    width=236.0,
    height=57)

entry1_img = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//img_textBox1.png")
entry1_bg = canvas.create_image(
    809.0, 390.0,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry1.place(
    x=694.0, y=359,
    width=230.0,
    height=60)

img0 = PhotoImage(
    file=f"C://Users//Rummy//Desktop//PRUEBA AGENTE\prueba_env//PANTALLA LOGIN//img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=717, y=489,
    width=181,
    height=41)

window.resizable(False, False)
window.mainloop()
"""

        
