from tkinter import *
import tkinter
from PIL import ImageTk, Image
a=Tk()
a.title("Analysis1")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)
image1 = Image.open('1.jpg').resize((1370,450))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)
image1 = Image.open('2.jpg').resize((1370,250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=450)


a.mainloop()
