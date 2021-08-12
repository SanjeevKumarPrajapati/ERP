from tkinter import *
import tkinter
from PIL import ImageTk, Image
import random
from tkinter import messagebox
import time
import os
a=Tk()
a.title("Home Page")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)
def exam():
    os.system("python Exam.py")
def lab1():
    messagebox.showwarning("Warning","No Data Found")
def notification():
    messagebox.showwarning("Warning","No Data Found")
def placement():
    messagebox.showwarning("Warning","No Data Found")
def event():
    messagebox.showwarning("Warning","No Data Found")
def academic():
    os.system("python Academic.py")
def fee():
    os.system("python fee.py")
def circular():
    os.system("python Circular.py")
def home():
    os.system("python Homepage.py")
def ana():
    os.system("python Analysis1.py")
    os.system("python Analysis2.py")
    os.system("python Analysis3.py")
image1 = Image.open('qulogo.jpg').resize((350,60))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

image1 = Image.open('analysis.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=900, y=10)
btn=Button(a,text="Analysis",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=ana).place(x=891,y=56)

image1 = Image.open('home.jpg').resize((50,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=980, y=10)
btn=Button(a,text="Home",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=home).place(x=986,y=56)


lb=Label(a,text="SANJEEV KUMAR PRAJAPATI",font=("Arial",12,"bold")).place(x=1050,y=20)
image1 = Image.open('myphoto.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=1300, y=10)

image1 = Image.open('myphoto.jpg').resize((150,150))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=100, y=100)
lb=Label(a,text="SANJEEV KUMAR PRAJAPATI",font=("Arial",14,"bold"),fg="#007FFF").place(x=30,y=260)


image1 = Image.open('message.jpg').resize((20,20))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=30, y=300)
lb=Label(a,text="sp6406919@gmail.com",font=("Arial",10,"bold"),fg="blue").place(x=60,y=300)

image1 = Image.open('phone.jpg').resize((20,20))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=30, y=330)
lb=Label(a,text="7900990614",font=("Arial",10,"bold"),fg="blue").place(x=60,y=330)

lb=Label(a,text="                   Father Name :        MOHAN LAL                                      ",font=("Arial",10),bg="#dff0d8").place(x=0,y=380)
lb=Label(a,text="                  Mother Name :        PREMWATI                                       ",font=("Arial",10),bg="#dff0d8").place(x=0,y=405)
lb=Label(a,text="                            D.O.B :        10/02/2001                                         ",font=("Arial",10),bg="#fcf8e3").place(x=0,y=430)
lb=Label(a,text="                          College :        Quantum School of Technology            ",font=("Arial",10),bg="#fcf8e3").place(x=0,y=455)
lb=Label(a,text="                           Course :        Bachelor of Technology                       ",font=("Arial",10),bg="#f2dede").place(x=0,y=480)
lb=Label(a,text="                 Specialization :        B.Tech (Hons.)                                   ",font=("Arial",10),bg="#f2dede").place(x=0,y=505)
lb=Label(a,text="                       Year/Sem :        5                                                             ",font=("Arial",10)).place(x=0,y=530)
lb=Label(a,text="                           Branch :        (Hons) in Computer Science and          ",font=("Arial",10),bg="#dff0d8").place(x=0,y=555)
lb=Label(a,text="                                               Engineering with specialization in         ",font=("Arial",10),bg="#dff0d8").place(x=0,y=585)
lb=Label(a,text="                                               Artificial Intelligence and Machine         ",font=("Arial",10),bg="#dff0d8").place(x=0,y=610)
lb=Label(a,text="                                               Learning                                             ",font=("Arial",10),bg="#dff0d8").place(x=0,y=635)
lb=Label(a,text="                          Section :        N/A                                                                 ",font=("Arial",10)).place(x=0,y=660)
lb=Label(a,text="                        Enroll No :        QU1901301065                                   ",font=("Arial",10),bg="#fcf8e3").place(x=0,y=685)

image1 = Image.open('aca.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=100)
btn=Button(a,text="Academic",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=academic).place(x=458,y=145)

image1 = Image.open('rupee2.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=175)
btn=Button(a,text="Fee",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=fee).place(x=475,y=220)

image1 = Image.open('circular.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=248)
btn=Button(a,text="Circular",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=circular).place(x=465,y=295)

image1 = Image.open('bell.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=323)
btn=Button(a,text="Notifications",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=notification).place(x=453,y=370)

image1 = Image.open('qulb.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=398)
btn=Button(a,text="Library",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=lab1).place(x=466,y=445)

image1 = Image.open('exam.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=473)
btn=Button(a,text="Exam",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=exam).place(x=472,y=520)

image1 = Image.open('place.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=548)
btn=Button(a,text="Placement",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=placement).place(x=457,y=595)

image1 = Image.open('event.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=470, y=623)
btn=Button(a,text="Event",bg="white",font=("Arial",8,"bold"),fg="#007FFF",command=event).place(x=470,y=670)

image1 = Image.open('right_side.jpg').resize((840,650))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=520, y=100)


a.mainloop()
