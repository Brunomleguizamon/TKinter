from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

img = Image.open('Tk.png')
# De esta manera se va a abrir la imagen con nuestro gestor predeterminado, en este caso Preview de Mac
#image.show()

# De esta manera toma la foto y la transforma en un tipo de dato que despues se puede usar en las etiquetas
imagen = ImageTk.PhotoImage(img)
l = Label(image=imagen)
l.pack()



root.mainloop()
