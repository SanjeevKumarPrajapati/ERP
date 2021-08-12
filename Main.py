from tkinter import *
import tkinter
from PIL import ImageTk, Image
import random
from tkinter import messagebox
import webbrowser as wb
import time
import os
a=Tk()
aa=random.randrange(0,10)
bb=random.randrange(0,10)
cc=random.randrange(0,10)
dd=random.randrange(0,10)
ee=random.randrange(0,10)
ff=random.randrange(0,10)
total=str(aa)+str(bb)+str(cc)+str(dd)+str(ee)+str(ff)
def login():
    a=var.get()
    b=var1.get()
    d=var2.get()
    if(a=="19030120"):
        if(b=="python"):
            if(d==total):
                os.system("python Homepage.py")
    if(a!="19030120"):
        messagebox.showwarning("Warning","Invalid ID")
    if(b!="python"):
        messagebox.showwarning("Warning","Invalid Password")
    if(d!=total):
        messagebox.showwarning("Warning","Invalid Captcha")
def cap():
    print(total)
def forget():
    abc=["a","b","c","d","e","f","g","h","i","j"]
    bcd=["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cde=["A","B","C","D","E","F","G","H","I","J"]
    dep=["K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lop=["0","1","2","3","4","5","6","7","8","9"]
    fod=["/","?","%","@","&","#","$","*"]
    xxx=random.choice(abc)+random.choice(bcd)+random.choice(cde)+random.choice(dep)+random.choice(lop)+random.choice(fod)
    a=input("Enter Your Q-Id :-")
    b=input("Email Id :-")
    print("Captcha :-",xxx)
    c=input("Enter captcha :-")
    if(a=="19030120"):
        if(b=="sp6406919@gmail.com"):
            if(c==xxx):
                print("Please wait.........")
                time.sleep(10)
                print("Your Password Updated successfully")
                pw="19030120"
                print("Your passwod is :- python")
            else:
                print("Please Enter Valid Captcha")
                forget()
    else:
        print("Please Enter Valid Details")
    login()
a.title("Login Page")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)


image1 = Image.open('QGChome.jpg').resize((1370,700))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

image1 = Image.open('white.jpg').resize((350,430))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=950, y=50)

var=StringVar()
et=Entry(a,fg="green",font=("Arial",19),borderwidth = 7,textvariable=var,bg="#fcf8e3").place(x=1000,y=170)
var1=StringVar()
et1=Entry(a,fg="green",font=("Arial",19),borderwidth = 7,textvariable=var1,show="*",bg="#fcf8e3").place(x=1000,y=240)
image1 = Image.open('qulogo.jpg').resize((350,90))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=950, y=50)
var2=StringVar()
et2=Entry(a,fg="green",font=("Arial",15),borderwidth = 7,textvariable=var2,bg="#fcf8e3").place(x=960,y=300)
btn=Button(a,text="Login",bd=6,bg="green",font=("Arial",16,"bold"),fg="white",command=login).place(x=1090,y=350)
btn=Button(a,text="Captcha",bd=5,bg="yellow",font=("Arial",13,"bold"),command=cap).place(x=1200,y=300)
btn=Button(a,text="Forgot Password",bd=6,bg="green",font=("Arial",16,"bold"),fg="white",command=forget).place(x=1030,y=420)
image1 = Image.open('user.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=950, y=170)

image1 = Image.open('password.jpg').resize((40,40))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=950, y=240)

image1 = Image.open('staff.jpg').resize((350,200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=950, y=490)
a.mainloop()
