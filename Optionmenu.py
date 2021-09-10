from tkinter import *

root = Tk()
root.title('Hello World: Option menu')
root.geometry('400x400')

def send():
    l = Label(root, text=value.get())
    l.pack()

lista = [ 
        'Enojado', 
        'Feliz', 
        'Triste'
        ]

value = StringVar()
value.set(lista[1])

drop = OptionMenu(root, value, *lista) # para pasarle argumento por argumento de la lista se utiliza el * antes 
drop.pack()

btn = Button(root, text='Send', command=send)
btn.pack()

root.mainloop()
