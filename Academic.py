from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os
import pyfiglet
from tkinter import messagebox
a=Tk()
a.title("Academic")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)
def home():
    os.system("python Homepage.py")
def ana():
    os.system("python Analysis1.py")
    os.system("python Analysis2.py")
    os.system("python Analysis3.py")
def syllabus():
    logo=pyfiglet.figlet_format("Syllabus")
    print(logo)
    print("=====================================================================================================================================")
    print("             Syllabus                                  Subject                               Subject Code     Subject Type    Credit")
    print("=====================================================================================================================================")
    print("1.)             ⬇              Demystifying Artificial Intelligence And Machine Learning         CS3321           Theory          3")
    print("2.)             ⬇              Python Programming                                                CS3322           Theory          3")
    print("3.)             ⬇              Python Programming Lab                                            CS3344          Practical        1")
    print("4.)             ⬇              Data Structure And Programming                                    CS3301           Theory          4")
    print("5.)             ⬇              Discreate Design Structure                                        CS3302           Theory          3")
    print("6.)             ⬇              Database Management System                                        CS3305           Theory          3")
    print("7.)             ⬇              Data Structure Programming Lab                                    CS3340          Practical        1")
    print("8.)             ⬇              Digital Electronics                                               EC3341          Practical        1")
    print("9.)             ⬇              Oracle/SQL Server Lab                                             CS3342          Practical        1")
    print("10.)            ⬇              Project Lab1                                                      CS3346          Practical        2")
    print("11.)            ⬇              Value Added Programe                                              VP3301          Practical        1")
    print("12.)            ⬇              Digital Electronic                                                EC3306           Theory          3")
    print("13.)            ⬇              Internship Presentation                                           CS3371          Practical        1")
    print("14.)            ⬇              General Proficiency                                               GP3301           Theory          1")
    print("=====================================================================================================================================")
def feedback():
    messagebox.showwarning("Warning","No Data Found")
def sem_reg():
    messagebox.showwarning("Warning","No Data Found")
def document():
    messagebox.showwarning("Warning","No Data Found")
def time_table():
        logo=pyfiglet.figlet_format("Time-Table")
        print(logo)
        print("=======================================================================================================================================================================")
        print("Days/Period	(P1)09:00-09:55	          (P2)09:55-10:50         (P3)10:50-11:45	 (P4)11:45-12:40	(P6)13:35-14:30	       (P7)14:30-15:25	(P8)15:25-16:20")
        print("=======================================================================================================================================================================")
        print("Monday	         Data Structure 	Digital Electronics	 Python Programming        -------------        Python Programming	  Project Lab	   Project Lab")
        print("\n")
        print("Tuesday	          Project Lab	            Project Lab		  ----------------     	   -------------             AIML                     VAP              VAP")
        print("\n")
        print("Wednesday	Data Structure 	         Data Structure      Discreate Design Structure	  Data Structure	     DBMS	            Oracle           Oracle")
        print("\n")
        print("Thrusday	--------------                DBMS	           Data Structure              DDS		     DDS                   -----------         AIML")
        print("\n")
        print("Frieday	     Digital Electronics	Digital Electronics  Discreate Design Structure	  --------------	 -----------------	     DBMS         -----------")
        print("\n")
        print("Saturday	    AIML	        Digital Electronics  Database Management System	  Data Structure 	Python Programming	 -------------	        DE")
        print("=======================================================================================================================================================================")
def assignment():
            logo=pyfiglet.figlet_format("Assignment")
            print(logo)
            print("================================================================================================================================================================")
            print("Download  Employee Name      Submit Date   Submit Start-End Time    Class Subject       Type      Assignment Subject      Uploaded Date    Max Marks    Obtained ")
            print("================================================================================================================================================================")
            print("   ⬇       SHADAB ALAM        19/09/2020   ----------------------      VAP(111)       Assignment      Assignment1           19/09/2020        15           11")
            print("   ⬇     CHANDANI SHARMA      19/09/2020   ----------------------    Digital Elec.    Assignment      Assignment1           19/09/2020        15           12")
            print("   ⬇      HIMANSHU TYAGI      30/09/2020   ----------------------       Python        Assignment      Assignment1           29/09/2020        15           15")
            print("   ⬇      SATENDER KUMAR      01/10/2020   ----------------------        DDS          Assignment      Assignment1           29/09/2020        15           13")
            print("   ⬇      MAHENDRA SWAIN      01/10/2020   ----------------------       AIML          Assignment      Assignment1           29/09/2020        15           13")
            print("   ⬇         SHALINI          30/09/2020   ----------------------       DBMS          Assignment      Assignment1           29/09/2020        15           13")
            print("   ⬇       SHADAB ALAM        16/10/2020   ----------------------      VAP(111)       Assignment      Assignment2           30/09/2020        15           NA")
            print("   ⬇       SHADAB ALAM        29/10/2020   ----------------------      VAP(111)       Assignment      Assignment3           16/10/2020        15           NA")
            print("   ⬇    SHOBHIT PRAJAPATI     19/09/2020   ----------------------    Data Structure   Assignment      Assignment1           29/10/2020        15           14")
            print("   ⬇         SHALINI          06/11/2020   ----------------------       DBMS          Assignment      Assignment2           05/11/2020        15           13")
            print("   ⬇     CHANDANI SHARMA      23/11/2020   ----------------------    Digital Elec.    Assignment      Assignment2           06/11/2020        15           12")
            print("   ⬇       HIMANSHU TYAGI     28/11/2020   ----------------------       Python        Assignment      Assignment2           23/11/2020        15           15")
            print("   ⬇      MAHENDRA SWAIN      30/11/2020   ----------------------       AIML          Assignment      Assignment2           26/11/2020        15           NA")
            print("   ⬇     SHOBHIT PRAJAPATI    28/11/2020   ----------------------    Data Structure   Assignment      Assignment2           26/11/2020        15           13")
            print("================================================================================================================================================================")
            
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
btn=Button(a,text="Time Table",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=time_table).place(x=90,y=80)
btn=Button(a,text="Assignment",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=assignment).place(x=85,y=160)
btn=Button(a,text="Syllabus",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=syllabus).place(x=100,y=240)
btn=Button(a,text="Feedback",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=feedback).place(x=95,y=320)
btn=Button(a,text="Semester Registration",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=sem_reg).place(x=40,y=400)
btn=Button(a,text="Document Upload",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=document).place(x=60,y=480)
lb=Label(a,text="Cyborg-ERP : Please Select Menu From Menu Bar.",font=("Arial",14,"bold"),fg="#007FFF").place(x=380,y=100)




















a.mainloop()
