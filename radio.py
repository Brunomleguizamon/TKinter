from tkinter import *

root = Tk()
root.title('Hola Mundo!')

r = IntVar()
r.set('2')


# Se elige la variable y el valor que va a asignarle a esta una vez elegido el campo
Radiobutton(root, text='Option 1', variable=r, value=1).pack()
Radiobutton(root, text='Option 2', variable=r, value=2).pack()

# Muestro la variable r
Label(root, textvariable=r).pack()

root.mainloop()
