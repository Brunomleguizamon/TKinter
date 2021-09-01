from tkinter import *
from tkmacosx import Button

root = Tk()
root.configure(background='#666')

root.title('Calculadora')
root.geometry('228x308')

equation = StringVar()

def press(num):
    equation.set(equation.get() + str(num))
    print(equation.get())

def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('Error')

def clear():
    equation.set('')

expression_entry = Entry(root, textvariable=equation,fg='#fff', background='#666', bd=3)
# Sticky para que tome todo el espacio disponible al norte sur este y oeste)
expression_entry.grid(row=0,columnspan=4, sticky='nswe', ipady=10)

# Botones
btnC = Button(root, text= ' C ', fg='#fff', background='#666', height = 50, width = 55, bd=1, command= clear)  
btnC.grid(column=0,row=1, sticky='nswe')
btnSigno = Button(root, text=' +/- ', fg='#fff', background='#666', height=50, width=55, bd=1)
btnSigno.grid(column=1, row=1)
btnPorcentaje = Button(root, text=' % ',fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press('%'))
btnPorcentaje.grid(column=2, row=1)
btnDiv = Button(root, text=' / ', fg='#fff', background='orange', height=50, width=55, bd=1, command=lambda: press('/'))
btnDiv.grid(column=3, row=1)

btn7 = Button(root, text=' 7 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(7))
btn7.grid(column=0,row=2)
btn8 = Button(root, text=' 8 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(8))
btn8.grid(column=1, row=2)
btn9 = Button(root, text=' 9 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(9))
btn9.grid(column=2, row=2)
btnMul = Button(root, text=' X ', fg='#fff', background='orange', height=50, width=55, bd=1, command=lambda: press('*')) 
btnMul.grid(column=3,row=2)

btn4 = Button(root, text=' 4 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(4))
btn4.grid(column=0, row=3)
btn5 = Button(root, text=' 5 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(5))
btn5.grid(column=1,row=3)
btn6 = Button(root, text=' 6 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(6))
btn6.grid(column=2, row=3)
btnRes = Button(root, text=' - ', fg='#fff', background='orange', height=50, width=55, bd=1, command=lambda: press('-'))
btnRes.grid(column=3, row=3)

btn1= Button(root, text= ' 1 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(1))
btn1.grid(column=0, row=4)
btn2= Button(root, text=' 2 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(2))
btn2.grid(column=1, row=4)
btn3 = Button(root, text=' 3 ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(3))
btn3.grid(column=2, row=4)
btnSuma= Button(root, text=' + ', fg='#fff', background='orange', height=50, width=55, bd=1, command=lambda: press('+'))
btnSuma.grid(column=3, row=4)

btn0 = Button(root, text=' 0 ', fg='#fff', background='#666', height=50, width=110, bd=1, command=lambda: press(0))
btn0.grid(columnspan=2, row=5)
btnComa = Button(root, text=' , ', fg='#fff', background='#666', height=50, width=55, bd=1, command=lambda: press(','))
btnComa.grid(column=2, row=5)
btnIgual= Button(root, text=' = ', fg='#fff', background='orange', height=50, width=55, bd=1, command= equalpress)
btnIgual.grid(column=3, row=5)

expression_entry.focus()
root.mainloop()
