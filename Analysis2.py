from tkinter import *
import tkinter
from PIL import ImageTk, Image
a=Tk()
a.title("Analysis2")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)
image1 = Image.open('3.jpg').resize((1370,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)
image1 = Image.open('4.jpg').resize((1370,500))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=200)


a.mainloop()
