from tkinter import *

root = Tk()
root.title('Hola Mundo!')

r = IntVar()
r.set('2')


ESTADOS = [ 
    ('Feliz','Feliz'),
    ('Triste','Triste'),
    ('Amargado','Amargado'),
    ('Enojado','Enojado')
        ]

varestado = StringVar()
varestado.set('Enojado')

for text, estado in ESTADOS:
    Radiobutton(root, text=text, variable= varestado , value=estado).pack()

# Se elige la variable y el valor que va a asignarle a esta una vez elegido el campo
#Radiobutton(root, text='Option 1', variable=r, value=1).pack()
#Radiobutton(root, text='Option 2', variable=r, value=2).pack()

# Muestro la variable r
Label(root, textvariable=varestado).pack()

root.mainloop()
