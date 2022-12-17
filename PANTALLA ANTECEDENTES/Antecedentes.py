from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x900")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA ANTECEDENTES//background.png")
background = canvas.create_image(
    433.5, 514.0,
    image=background_img)

canvas.create_text(
    525.0, 74.0,
    text = "ANTECEDENTES",
    fill = "#000000",
    font = ("None", int(30.0)))

img0 = PhotoImage(file = f"C://Users//Rummy//Desktop//PRUEBA AGENTE//prueba_env//PANTALLA ANTECEDENTES//img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 401, y = 800,
    width = 249,
    height = 55)

window.resizable(False, False)
window.mainloop()
