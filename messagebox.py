from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola Mundo')

def click():
    # Alerta de alarma
    messagebox.showwarning('Popup', 'Hola Mundo!')
    # Alerta de informacion
    messagebox.showinfo('Popup','Hola')
    # Alerta de Error
    messagebox.showerror('Popup','Error')

def click1():
    # Se utiliza para hacer preguntas al usuario y capturar su respuesta
    # esta devuelve un STRING
    respuesta = messagebox.askquestion('Popup', 'Necesito preguntarte algo')    
    print(respuesta)
    if respuesta == 'yes':
        messagebox.showinfo('Popup', 'la respuesta fue YES')
    else:
        messagebox.showinfo('Popup', 'la respuesta fue NO')
    
def click2():
    # Pregunta ok cancel este devuelve True o False
    # esta devuelve un Boolean
    respuesta = messagebox.askokcancel('Popup', 'Deseas continuar?')
    print(respuesta)
    if respuesta == True:
        messagebox.showinfo('Popup', 'Seleccionaste Ok')
    else:
        messagebox.showinfo('Popup', 'Seleccionaste Cancelar')
def click3():
    # Pregunta ok cancel este devuelve True o False
    # esta devuelve un Boolean
    respuesta = messagebox.askyesno('Popup', 'Deseas continuar?')
    print(respuesta)
    if respuesta == True:
        messagebox.showinfo('Popup', 'Seleccionaste Ok')
    else:
        messagebox.showinfo('Popup', 'Seleccionaste Cancelar')


btn = Button(root, text='Presioname', command= click3)
btn.pack()

root.mainloop()
