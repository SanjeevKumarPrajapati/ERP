from tkinter import *
import tkinter
import pyfiglet
from PIL import ImageTk, Image
import numpy as np
from tkinter import messagebox
import matplotlib.pyplot as plt
a=Tk()
a.title("Analysis3")
a.iconbitmap("Quantum-logo.ico")#for icon
a.minsize(1370,700)
a.maxsize(1370,700)
def att():
    present=[44,48,25,57,59,59,26,28,30,56,28,40]
    total=[44,48,25,57,59,59,26,28,30,56,28,40]
    percent=[100,100,100,100,100,100,100,100,100,100,100,100,]
    x=np.arange(len(present))
    a=[44,48,25,57,59,59,26,28,30,56,28,40]
    b=['CS3321','CS3322','CS3344','CS3302','CS3305','CS3340','CS3340','EC3341','CS3342','CS3346','VP3301','EC33206']
    plt.pie(a,labels=b,explode=(0.2,0.2,0,0,0,0,0,0,0,0,0,0.2),autopct='%1.1f%%')
    plt.title("Subject wise Attendance Details")
    plt.axis('equal')
    plt.legend(['CS3321','CS3322','CS3344','CS3302','CS3305','CS3340','CS3340','EC3341','CS3342','CS3346','VP3301','EC33206'])
    plt.xlabel("Subject Code")
    plt.ylabel("Subject %")
    plt.figure(figsize=[5,10])
    #bar plot
    plt.bar(x,present,color='blue',width=0.12)
    plt.bar(x+0.12,total,color='red',width=0.12)
    plt.bar(x+0.12+0.12,percent,color='orange',width=0.12)
    plt.legend(['Present','Total','Percent'])
    plt.xticks([i+0.25 for i in range(12)],['CS3321','CS3322','CS3344','CS3302','CS3305','CS3340','CS3340','EC3341','CS3342','CS3346','VP3301','EC33206'])
    plt.title("Subject wise Attendance Details")
    plt.xlabel("Subjects")
    plt.xlabel("Subject Code")
    plt.ylabel("Subject %")
    plt.show()
    plt.show()
def mon_reg():
    x=var.get().lower()
    if(x=="august"):
        logo=pyfiglet.figlet_format("August")
        print(logo)
        print("=======================================================================================================================================================================")
        print("	                    Subject             1       2       3       4       5       6       7       8       9       10      11      12      13      14      15\n\t\t\t\t\t\t16      17      18      19      20      21      22      23      24      25      26      27      28      29      30")
        print("=======================================================================================================================================================================")
        print("1	CS3321 (Demystifying AIML	        N	N	N	N	N	N	N	N	N	N	N	N	P	N	N	\n\t\t\t\t\t\tN	N	P	N	P	N	P	N	N	P	N	P	N	P	N")	
        print("2	CS3322 (Python Programming(S))	        N	N	N	N	N	N	N	N	N	N	N	N	N	P	N	\n\t\t\t\t\t\tN	P	N	N	N	P	P	N	P	N	N	N	P	P	N")	
        print("3	CS3344 (Python Programming Lab(L))	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N	N")	
        print("4	CS3301 (Data Structure a	        N	N	N	N	N	N	N	N	N	N	N	N	P	N	N	\n\t\t\t\t\t\tN	P	N	P	P	N	P	N	N	N	P	P	P	P	N")	
        print("5	CS3302 (Discrete Design Structure	N	N	N	N	N	N	N	N	N	N	N	N	P	P	N	\n\t\t\t\t\t\tN	N	P	P	P	P	N	N	N	P	P	P	N	N	N")	
        print("6	CS3305 (Database Management System(S))	N	N	N	N	N	N	N	N	N	N	N	N	P	P	N	\n\t\t\t\t\t\tN	N	N	P	P	P	P	N	N	N	P	P	P	P	N")	
        print("7	CS3340 (Data Structure Programming Lab	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	P,P	N	N	N	N")	
        print("8	EC3341 (Digital Electronics Lab(L))	N	N	N	N	N	N	N	N	N	N	N	N	N	P,P	N	\n\t\t\t\t\t\tN	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N")	
        print("9	CS3342 (Oracle/SQL Server Lab(L))	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N")	
        print("10	CS3346 (Project Lab I(L))	        N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	P,P	P,P	N	N	N	N	N	P,P	P,P	N	N	N	N	N")	
        print("11	VP3301 (Value Added Program III(L))	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	P,P	N	N	N	N	N")	
        print("12	EC3306 (Digital Electronics(S))   	N	N	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	P	N	N	N	N	P,P	N	P	N	N	N	N	P,P	N")	
        print("=======================================================================================================================================================================")
    elif(x=="september"):
        logo=pyfiglet.figlet_format("September")
        print(logo)
        print("=======================================================================================================================================================================")
        print("	                    Subject             1       2       3       4       5       6       7       8       9       10      11      12      13      14      15\n\t\t\t\t\t\t16      17      18      19      20      21      22      23      24      25      26      27      28      29      30")
        print("=======================================================================================================================================================================")
        print("1        CS3321 (Demystifying AI And ML   	P	N	P	N	P	N	N	P	N	P	N	P	N	N	P	\n\t\t\t\t\t\tN	P	N	P	N	N	P	N	P	N	P	N	N	P	N")
        print("2	CS3322 (Python Programming(S))	        N	N	N	P	P	N	P	N	N	N	P	P	N	P	N	\n\t\t\t\t\t\tN	N	P	P	N	P	N	N	N	P	P	N	P	N	N")
        print("3	CS3344 (Python Programming Lab(L))	N	N	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N	\n\t\t\t\t\t\tN	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N")
        print("4	CS3301 (Data Structure and Programming	N	N	P	P	P	N	N	N	P	P	N	P	N	P	N	\n\t\t\t\t\t\tP	P	N	P	N	P	N	P	P	N	P	N	P	N	P")
        print("5	CS3302 (Discrete Design Structur)	P	N	P	N	N	N	N	N	P	P,P	P	N	N	N	N	\n\t\t\t\t\t\tP	P,P	P	N	N	N	N	P	P,P	P	N	N	N	N	P")
        print("6	CS3305 (Database Management System(S))	N	N	P	P	P	N	N	N	P	P	P	P	N	N	N	\n\t\t\t\t\t\tP	P	P	P	N	N	N	P	P	P	P	N	N	N	P")
        print("7	CS3340 (Data Structure Programming Lab	N	N	N	N	N	N	N	N	P,P	N	N	N	N	N	N	\n\t\t\t\t\t\tP,P	N	N	N	N	N	N	P,P	N	N	N	N	N	N	P,P")
        print("8	EC3341 (Digital Electronics Lab(L))	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	\n\t\t\t\t\t\tN	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N")
        print("9	CS3342 (Oracle/SQL Server Lab(L))	N	N	N	N	N	N	N	N	P,P	N	N	N	N	N	N	\n\t\t\t\t\t\tP,P	N	N	N	N	N	N	P,P	N	N	N	N	N	N	P,P")
        print("10	CS3346 (Project Lab I(L))	        P,P	N	N	N	N	N	P,P	P,P	N	N	N	N	N	P,P	P,P	\n\t\t\t\t\t\tN	N	N	N	N	P,P	P,P	N	N	N	N	N	P,P	P,P	N")
        print("11	VP3301 (Value Added Program III(L))	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N")
        print("12	EC3306 (Digital Electronics(S))	N	N	N	N	P,P	N	P	N	N	N	N	P,P	N	P	N	N	\n\t\t\t\t\t\tN	N	P,P	N	P	N	N	N	N	P,P	N	P	N	N       N")
        print("=======================================================================================================================================================================")
    elif(x=="october"):
        logo=pyfiglet.figlet_format("October")
        print(logo)
        print("=======================================================================================================================================================================")
        print("	                    Subject             1       2       3       4       5       6       7       8       9       10      11      12      13      14      15\n\t\t\t\t\t\t16      17      18      19      20      21      22      23      24      25      26      27      28      29      30")
        print("=======================================================================================================================================================================")
        print("1	CS3321 (Demystifying AIML	        P	N	P	N	N	P	N	P	N	P	N	N	P	N	P	\n\t\t\t\t\t\tN	P	N	N	N	N	N	N	N	N	N	P	N	P	N")
        print("2	CS3322 (Python Programming(S))	        N	N	P	N	P	N	N	N	P	P	N	P	N	N	N	\n\t\t\t\t\t\tP	P	N	N	N	N	N	N	N	N	N	N	N	N	P")
        print("3	CS3344 (Python Programming Lab     	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("4	CS3301 (Data Structure and Programming	P	N	P	N	P	N	P	P	N	P	N	P	N	P	P	\n\t\t\t\t\t\tN	P	N	N	N	N	N	N	N	N	N	N	P	P	N")
        print("5	CS3302 (Discrete Design Structure(S))	P,P	N	N	N	N	N	P	P,P	P	N	N	N	N	P	P,P	\n\t\t\t\t\t\tP	N	N	N	N	N	N	N	N	N	N	N	P	P,P	P")	
        print("6	CS3305 (Database Management System(S))	P	N	P	N	N	N	P	P	P	P	N	N	N	P	P	\n\t\t\t\t\t\tP	P	N	N	N	N	N	N	N	N	N	N	P	P	P")	
        print("7	CS3340 (Data Structure Programming Lab	N	N	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	P,P	N	N")	
        print("8	EC3341 (Digital Electronics Lab(L))	N	N	N	N	N	N	N	N	P,P	N	N	N	N	N	N	\n\t\t\t\t\t\tP,P	N	N	N	N	N	N	N	N	N	N	N	N	P,P")	
        print("9	CS3342 (Oracle/SQL Server Lab(L))	N	N	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	P,P	N	N")	
        print("10	CS3346 (Project Lab I(L))	        N	N	N	N	P,P	P,P	N	N	N	N	N	P,P	P,P	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	P,P	N	N	N")	
        print("11	VP3301 (Value Added Program III(L))	N	N	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	P,P	N	N	N")	
        print("12	EC3306 (Digital Electronics(S))	        N	N	P,P	N	P	N	N	N	N	P,P	N	P	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")	
        print("=======================================================================================================================================================================")
    elif(x=="november"):
        logo=pyfiglet.figlet_format("November")
        print(logo)
        print("=======================================================================================================================================================================")
        print("	                    Subject             1       2       3       4       5       6       7       8       9       10      11      12      13      14      15\n\t\t\t\t\t\t16      17      18      19      20      21      22      23      24      25      26      27      28      29      30")
        print("=======================================================================================================================================================================")
        print("1	CS3321 (Demystifying AIML        	N	N	P	N	P	N	N	N	N	P	N	P	N	N	N	\n\t\t\t\t\t\tN	P	N	P	N	P	N	N	P	N	P	N	P	N	N")
        print("2	CS3322 (Python Programming(S))	        N	P	N	N	N	P	P	N	P	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	P	N	P	N	N	N	N	P	N	P")
        print("3	CS3344 (Python Programming Lab(L))	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	P	N	N	N	N	N	N	P")
        print("4	CS3301 (Data Structure and Programming	N	P	N	P	P	N	P	N	P	N	P	P	N	N	N	\n\t\t\t\t\t\tN	N	P	P	N	P	N	P	N	P	P	N	P	N	P")
        print("5	CS3302 (Discrete Design Structure)	N	N	N	P	P,P	P	N	N	N	N	P	P,P	N	N	N	\n\t\t\t\t\t\tN	N	P	P,P	P	N	N	N	N	P	P,P	P	N	N	N")
        print("6	CS3305 (Database Management System(S))	N	N	N	P	P	P	P	N	N	N	P	P	N	N	N	\n\t\t\t\t\t\tN	N	P	P	P	P	N	N	N	P	P	P	P	N	N")
        print("7	CS3340 (Data Structure Programming)	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	\n\t\t\t\t\t\tN	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N")
        print("8	EC3341 (Digital Electronics Lab(L))	N	N	N	N	N	P,P	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N	N")
        print("9	CS3342 (Oracle/SQL Server Lab(L))	N	N	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	\n\t\t\t\t\t\tN	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N")
        print("10	CS3346 (Project Lab I(L))	        N	P,P	P,P	N	N	N	N	N	P,P	P,P	N	N	N	N	N	\n\t\t\t\t\t\tP,P	N	N	N	N	N	P,P	P,P	N	N	N	N   	N    P,P")
        print("11	VP3301 (Value Added Program III(L))	N	N	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N	\n\t\t\t\t\t\tN	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N	N")
        print("12	EC3306 (Digital Electronics(S))	        N	P	N	N	N	N	P,P	N	P	N	N	N	N	N	N	s\n\t\t\t\t\t\tN	N	N	N	P,P	N	P	N	N	N	N	P,P	N       N")
        print("=======================================================================================================================================================================")
    elif(x=="december"):
        logo=pyfiglet.figlet_format("December")
        print(logo)
        print("=======================================================================================================================================================================")
        print("	                    Subject             1       2       3       4       5       6       7       8       9       10      11      12      13      14      15\n\t\t\t\t\t\t16      17      18      19      20      21      22      23      24      25      26      27      28      29      30")
        print("=======================================================================================================================================================================")
        print("1	CS3321 (Demystifying AIML	        P	N	P	N	P	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("2	CS3322 (Python Programming(S))	        N	N	N	N	P	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("3	CS3344 (Python Programming Lab	        N	N	N	N	N	N	P	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("4	CS3301 (Data Structure and Programming	N	P	P	N	P	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("5	CS3302 (Discrete Design Structure)	N	P	P,P	P	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("6	CS3305 (Database Management System(S))	N	N	P	P	P	N	N	N	P	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("7	CS3340 (Data Structure Programming Lab	N	P,P	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("8	EC3341 (Digital Electronics Lab(L))	N	N	N	P,P	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("9	CS3342 (Oracle/SQL Server Lab(L))	N	P,P	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("10	CS3346 (Project Lab I(L))	        P,P	N	N	N	N	N	N	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("11	VP3301 (Value Added Program III(L))	P,P	N	N	N	N	N	N	P,P	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("12	EC3306 (Digital Electronics(S))	        N	N	N	N	P,P	N	P	N	N	N	N	N	N	N	N	\n\t\t\t\t\t\tN	N	N	N	N	N	N	N	N	N	N	N	N	N	N")
        print("=======================================================================================================================================================================")
    else:
        messagebox.showwarning("Warning","No Data Found")
image1 = Image.open('5.jpg').resize((1370,450))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

image1 = Image.open('6.jpg').resize((1050,50))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=450)
bt1=Button(a,text="        View Attendance        ",bd=7,bg="red",font=("Arial",15,"bold"),fg="white",command=att).place(x=1060,y=450)
image1 = Image.open('7.jpg').resize((1370,120))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=510)

image1 = Image.open('8.jpg').resize((600,50))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=640)
var=StringVar()
et=Entry(a,fg="green",font=("Arial",20),borderwidth = 7,textvariable=var).place(x=630,y=645)
bt1=Button(a,text="                    View                    ",bd=7,bg="red",font=("Arial",15,"bold"),fg="white",command=mon_reg).place(x=1030,y=645)
a.mainloop()