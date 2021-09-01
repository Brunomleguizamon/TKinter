from tkinter import *

root = Tk()
root.title('Hola mundo')

#pad en LabelFrame agrega un padding interno
frame = LabelFrame(root, text='Login',padx=20, pady=20, borderwidth=5)
#tambien se puede crear un frame pero sin marcos utilizando:
#frame = Frame(root, padx=20, pady=20)

#pad en pack agrega un padding externo
frame.pack(padx=50, pady=50)


l = Label(frame, text='estoy dentro de un frame')
btn = Button(frame, text='salir', command=root.quit)

l.pack()
btn.pack()



root.mainloop()
