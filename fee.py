from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os
import pyfiglet
from tkinter import messagebox
a=Tk()
a.title("Fee")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)
def home():
    os.system("python Homepage.py")
def ana():
    os.system("python Analysis1.py")
    os.system("python Analysis2.py")
    os.system("python Analysis3.py")
def fee():
        logo=pyfiglet.figlet_format("Fee")
        print(logo)
        print("\n\t<------- Academic Fee Details( Amount in --------->\n")
        print("====================================================================================================================================")
        print("       Sem/Year          Fee Head          Current Dues Amount        Scholarship/Discounnt        Paid Amount        Balance Amount  ")
        print("====================================================================================================================================")
        print("1.)    3rd Sem       Branch Change Fee         15,000.00                      0.00                    0.00               15,000.00")
        print("2.)    3rd Sem         TUITION Fee             42,000.00                      0.00                  40,000.00             2,500.00")
        print("3.)    3rd Sem       ACADEMIC SERVICES         17,500.00                      0.00                  12,500.00             5,000.00")
        print("4.)    3rd Sem           EXAM FEE              2,500.00                       0.00                   2,500.00               0.00")
        print("5.)    4th Sem         TUITION FEE             42,500.00                      0.00                  22,500.00            20,000.00")
        print("6.)    4th Sem       ACADEMIC SERVICES         17,500.00                      0.00                    0.00               17,500.00")
        print("7.)    4th Sem           EXAM FEE              2,500.00                       0.00                    0.00                2,500.00")
        print("====================================================================================================================================")
        
def fee_sub():
    messagebox.showwarning("Warning","No Data Found")
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
btn=Button(a,text="Fee Submission",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=fee).place(x=90,y=80)
btn=Button(a,text="Transaction History",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=fee_sub).place(x=65,y=160)
lb=Label(a,text="Cyborg-ERP : Please Select Menu From Menu Bar.",font=("Arial",14,"bold"),fg="#007FFF").place(x=380,y=100)













a.mainloop()
