from tkinter import *

root = Tk()
root.title('Hello World: Checkbox')
root.geometry('400x400')

var = StringVar()
# se le puede colocar un valor por defecto para que no muestre - al iniciar el checkbutton
var.set('No')

def show():
    v = var.get()
    l = Label(root, text=v)
    l.pack()

c = Checkbutton(root, text='I am checkbutton', variable=var, onvalue='Yes', offvalue='No')
c.pack()

btn= Button(root, text='Click', command=show)
btn.pack()

root.mainloop()
