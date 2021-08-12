from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os
import pyfiglet
from tkinter import messagebox
a=Tk()
a.title("Circular")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)
def home():
    os.system("python Homepage.py")
def ana():
    os.system("python Analysis1.py")
    os.system("python Analysis2.py")
    os.system("python Analysis3.py")
def circular():
    logo=pyfiglet.figlet_format("Circular")
    print(logo)
    print("\n\t<------- Circular Details --------->")
    print("=======================================================================================================================================")
    print("                                             Subject                                   Date  Form          Date To         Circular By")
    print("=======================================================================================================================================")
    print("\n")
    print("1.)    Transport Notice for 1st Year student Only                                      22/12/2020        31/12/2020       RAVINDER GIRI")
    print("2.)    Pin click will be conducting drive for post Graduates and under Graduates       22/12/2020        31/12/2020       RAVINDER GIRI")
    print("3.)    Diploma 1st year New Time Table Effective From 23.12.2020                       22/12/2020        31/12/2020       RAVINDER GIRI")
    print("4.)    Pharmacy 1st year New Time Table Efffective From23.12.2020                      22/12/2020        31/12/2020       RAVINDER GIRI")
    print("5.)    Nutrition & Dietetics 1st year New Time Table Effective From 23.12.2020         22/12/2020        31/12/2020       RAVINDER GIRI")
    print("6.)    MCA 1st year New Time Table Effective Form23.12.2020                            22/12/2020        31/12/2020       RAVINDER GIRI")
    print("7.)    BMRIT 1st year New Time Table Effective Form23.12.2020                          22/12/2020        31/12/2020       RAVINDER GIRI")
    print("8.)    BJMC 1st year New Time Table Effective Form23.12.2020                           22/12/2020        31/12/2020       RAVINDER GIRI")
    print("9.)    BCA 1st year New Time Table Effective Form23.12.2020                            22/12/2020        31/12/2020       RAVINDER GIRI")
    print("10.)   B.TECH 1st year New Time Table Effective Form23.12.2020                         22/12/2020        31/12/2020       RAVINDER GIRI")
    print("11.)   B.Sc PCM 1st year New Time Table Effective Form23.12.2020                       22/12/2020        31/12/2020       RAVINDER GIRI")
    print("=======================================================================================================================================")

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
btn=Button(a,text="Circular",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=circular).place(x=90,y=80)
lb=Label(a,text="Cyborg-ERP : Please Select Menu From Menu Bar.",font=("Arial",14,"bold"),fg="#007FFF").place(x=380,y=100)

a.mainloop()
