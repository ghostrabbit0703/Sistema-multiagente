from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x700")
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

background_img = PhotoImage(file = f"prueba_env//PANTALLA SELECCION//background.png")
background = canvas.create_image(
    485.5, 500.5,
    image=background_img)

entry0_img = PhotoImage(file = f"prueba_env//PANTALLA SELECCION///img_textBox0.png")
entry0_bg = canvas.create_image(
    373.0, 371.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f9f2f2",
    highlightthickness = 0)

entry0.place(
    x = 82, y = 128,
    width = 582,
    height = 485)

img0 = PhotoImage(file = f"prueba_env//PANTALLA SELECCION//img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 698, y = 128,
    width = 212,
    height = 51)

img1 = PhotoImage(file = f"prueba_env//PANTALLA SELECCION//img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 698, y = 214,
    width = 212,
    height = 54)

window.resizable(False, False)
window.mainloop()
