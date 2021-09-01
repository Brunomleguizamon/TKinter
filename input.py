from tkinter import *

root = Tk()
root.title('Hola Mundo')
root.geometry('550x350')

# para definir un input se llama a Entru() y este recibe los argumentos de:
# 1ro donde se va a renderizar el input, 2do cuanto va a ser el ancho el input
e = Entry(root, width=40)
# utilizo pack para mostrar el widget
e.pack()
# Mostrar datos desde alguna base de datos o manualmente
e.insert(0, 'Ingresa texto:')

def click():
    texto = e.get()
    # para setear el texto de text varible se ultiliza
    textvariable.set(texto)
    # tambien se puede recuperar el valor de este
    contenido = textvariable.get()
    print(contenido)

    '''
    # utilizo .get() para tomar el valor de e
    texto = e.get()
    # utilizo .configure() para cambiar el valor de la etiqueta, en este caso el texto por lo tomado desde e
    l.configure(text=texto)
    '''
    # Elimino el contenido dentro del campo
    e.delete(0, END)
    

#l = Label(root, text='texto de la etiqueta')
#l.pack()

btn = Button(root, text='click', command=click)
btn.pack()

# se puede setear un texto con una variable itilizando textvariable
textvariable = StringVar()
l = Label(root, textvariable=textvariable)
l.pack()

root.mainloop()
