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
        self.ax.set_xlabel("Muestra", color='#00ff00')
        self.ax.set_ylabel("Muestra", color='#00ff00')
        self.ax.tick_params(direction='out',length=6, width=2,colors='#00ff00',grid_color='black',grid_alpha=1)
        
        self.frame1 = Frame(self.master,bg='red')
        self.frame1.grid(column=0,row=0,sticky='nsew')

        self.frame2 = Frame(self.master,bg='black')
        self.frame2.grid(column=1,row=0,sticky='nsew')

        self.canvas=FigureCanvasTkAgg(self.fig, master=self.frame1)
        self.canvas.get_tk_widget().pack(expand=True)

        Button(self.frame2,text='Graficar datos',bg='magenta',command=self.obtener_datos).pack(expand=True)

    def obtener_datos(self):
        self.sql=("SELECT pd,dp FROM universitario_has_test INNER JOIN test on idtest=test_idtest where universitario_iduniversitario =1")
        self.dbpsi.cursor.execute(self.sql)
        self.datos=self.dbpsi.cursor.fetchall()
    def graficar_dadtos(self):
        x=[]
        n=[]
        for i in self.datos:
            a= i[0]
            b= i[1]
            n.append(a)
            x.append(b)
        self.ax.plot(n,x,color='b', linestyle='solid')
        self.canvas.draw()
        plt.grid(alpha=0.5)

if __name__ == "__main__":
    ventana=Tk()
    ventana.geometry('730x400')
    ventana.resizable(0,0)
    ventana.config(bg='black')
    ventana.wm_title('Grafica')
    app = Grafica(ventana)
    app.mainloop()
print(__name__)
     
"""from tkinter import *
from LOGIN import *


def main():
    root = Tk()
    root.wm_title("LOGIN")
    app = LOGIN(root)
    app.mainloop()


if __name__ == "__main__":
    main()
"""