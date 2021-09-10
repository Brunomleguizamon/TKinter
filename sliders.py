from tkinter import *

root = Tk()
root.title('Hello World: Sliders')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

# Como comnsultar el valor del slider

def enviar():
    hor = horizontal.get()
    ver = vertical.get()
    print(str(hor) + ' ' + str(ver))
    return ver, hor

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()
