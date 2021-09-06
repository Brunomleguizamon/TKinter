from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

# Solucion 1 al problema de que no muestra la imagen si no ejecuto mainloop()
'''
def Open():
    img = ImageTk.PhotoImage(Image.open('Tk.png'))
    # con Toplevel indicamos que debe abrir otra ventana
    top = Toplevel()
    top.title('Hola Mundo desde otra ventana')
    l = Label(top, text= 'Soy un texto desde una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()
'''

# Solucion 2

def Open():
    global img
    img = ImageTk.PhotoImage(Image.open('Tk.png'))
    top = Toplevel()
    top.title('Hola Mundo desde otra ventana')
    l = Label(top, text= 'Soy un texto desde una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

# Solucion 3 pasarle la variable de imagen como argumento
def Open(img):
    top = Toplevel()
    top.title('Hola Mundo desde otra ventana')
    l = Label(top, text= 'Soy un texto desde una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open('Tk.png'))
btn = Button(root, text='New Window', command=lambda: Open(img)).pack()

root.mainloop()
