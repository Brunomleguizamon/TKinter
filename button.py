from tkinter import *

root = Tk()
root.title('Hola Mundo')

# si l esta fuera de la funcion va a ser agregado solo una vez cuando la funcion sea llamda
l = Label(root, text='Hola Mundo!')

def click():
    # si l esta dentro de la funcion cada vez que sea llamdo se va añadir una nueva
    #l = Label(root, text='Hola mundo!')
    l.pack()

# Se crea botones con Button() este recibe una serie de argumentos
# 1ro donde queremos que sea renderizado, 2do el texto que muestra el boton
# 3ro se debe agregar el argumento que va a indicar la funcion a ejecutar
# 4to fg cambiar el color del texto, 5to bg para cambiar el background (este no funciona en MacOs)
btn = Button(root, text='Clickeame', command=click, fg='red', bg='blue')
# Luego hay que mostrar el boton con .pack()
btn.pack()


root.mainloop()

