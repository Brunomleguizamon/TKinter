from tkinter import *

root = Tk()
root.title('Pies a Metros')


intro = Frame(root, padx=12, pady=3)
intro.grid(column=0, row=0)
Label(intro, text='Esta aplicacion realiza la conversion de pies a metros').grid(column=0,row=0)
Label(intro, text='se ingresa valor en pies, y se obtiene valor en metros').grid(column=0,row=1)

def calcular(*args):
    try:
        value = float(pies.get())
        m = int(0.3048 * value * 10000 + 0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set('ERROR')

frame = Frame(root, padx=12, pady=3)
frame.grid(column=0, row=1)

pies = StringVar()
pies_input= Entry(frame, width=7, textvariable=pies)
pies_input.grid(column=1, row=0)

metros = StringVar()
Label(frame, textvariable=metros).grid(column=1, row=1)

Button(frame, text='calcular', command=calcular).grid(column=2, row=2)

Label(frame, text='Pies').grid(column=0, row=0)
Label(frame, text='Es igual a').grid(column=0, row=1)
Label(frame, text='metros').grid(column=2, row=1)

# Con .focus hace que apenas abra la aplicacion el cursor se encuentre en este campo
pies_input.focus()
# Permite escuchar eventos y realizar acciones, 
# por ejemplo en este caso va a escuchar el enter y llamar a la funcion calcular 
root.bind("<Return>", calcular)

root.mainloop()
