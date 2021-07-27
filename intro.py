from tkinter import *

# Iniciar la aplicacion
root = Tk()

# Titulo de la aplicacion
root.title('Hola Mundo')

# Dimenciones de la ventana, ancho y alto
root.geometry('550x350')

# Widget label (etiqueta)
# Recibe dos argumentos 1ª Donde quiero renderizarlo 2ª Texto
label = Label(root, text='Hola mundo!')
# Se indica que se muestre la etiqueta con .pack()
#label.pack()
# Como python es un lenguaje orientado a objetos no es necesario crear una nueva instancia de label
# y luego se la asignemos a una funcion para luego llamar a pack, sino que se puede hacer de esta manera:
#Label(root, text='Hola mundo! mi primera etiqueta desde POO').pack()

l1 = Label(root, text='Hola mundo! primera etiqueta')
l2 = Label(root, text='Chau mundo! segunda etiqueta')

# Otra manera de mostrar nuestra etiqueta es con .grid() el cual usa un sistema de grilla
l1.grid(row=0, column=0)
l2.grid(row=0, column=1)

# Instruccion para que Tk se quede escuchando a posibles cambios
root.mainloop()

