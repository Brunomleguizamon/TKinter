from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Hello World: Files')

def open():
    global imgTk
    root.filename = filedialog.askopenfilename(title= 'Choose your file', filetypes=(('png files', '*.png'),
                                                                                ('jpeg files', '*.jpeg') ,
                                                                                ('all' ,'*' )))
    l = Label(root, text=root.filename)
    l.pack()
    img = Image.open(root.filename)
    imgTk = ImageTk.PhotoImage(img)
    l2 = Label(root, image=imgTk)
    l2.pack()

btn = Button(root, text='Open file', command=open)
btn.pack()

root.mainloop()
