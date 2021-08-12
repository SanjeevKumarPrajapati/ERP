from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os
import pyfiglet
from tkinter import messagebox
a=Tk()
a.title("Exam")
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
    messagebox.showwarning("Warning","No Data Found")
def external():
        logo=pyfiglet.figlet_format("Assignment")
        print(logo)
        print("\n\t<------- Sessional/Teacher Assessment Marks Statement --------->\n")
        print("Student Name")
        print("SANJEEV KUMAR PRAJAPATI\n")
        print("Father Name")
        print("MOHAN LAL\n")
        print("Enrollment No")
        print("QU1901301065\n")
        print("Course")
        print("B.Tech\n")
        print("Branch")
        print("(Hons.)Computer Science & Engineering with\nSpecialization in AI and Machine Learning in\nCollaboration with Xebia")
        def exam_in():
            a=int(input("\n\tSemester : "))
            b=input("\n\tSubject Type[Theory,Practical] : ").lower()
            c=int(input("\n\tSessional/TA : "))
            d=input("\n\tFor Exit Press E and Continue C[E/C] :").lower()
            if(a==1 and b=='theory' and c==1 and d=='c'):
                print("\n")
                print("==============================================================================================================================")
                print("                Subject                  Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("==============================================================================================================================")
                print("1.)  Engineering Physics                    PH3101                  Sessioonal-1                    45                50")
                print("2.)  Mathematics - 1                        MH3102                  Sessioonal-1                    40                50")
                print("3.)  Professional Communication             EG3102                  Sessioonal-1                    39                50")
                print("4.)  Basic of Computer and C Programming    CS3101                  Sessioonal-1                    43                50")
                print("5.)  Basic Machanical Engineering           ME3102                  Sessioonal-1                    42                50")
                print("6.)  Disaster Management                    CE3101                  Sessioonal-1                    42                50")
                print("==============================================================================================================================")
                exam_in()
            elif(a==1 and b=='theory' and c==2 and d=='c'):
                print("\n")
                print("==============================================================================================================================")
                print("                Subject                  Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("==============================================================================================================================")
                print("1.)  Engineering Physics                    PH3101                  Sessioonal-2                    46                50")
                print("2.)  Mathematics - 1                        MH3102                  Sessioonal-2                    50                50")
                print("3.)  Professional Communication             EG3102                  Sessioonal-2                    41                50")
                print("4.)  Basic of Computer and C Programming    CS3101                  Sessioonal-2                    46                50")
                print("5.)  Basic Machanical Engineering           ME3102                  Sessioonal-2                    34                50")
                print("6.)  Disaster Management                    CE3101                  Sessioonal-2                    36                50")
                print("==============================================================================================================================")
                exam_in()
            elif(a==1 and b=='theory' and c>2 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(a==1 and b=='practical' and c==1 and d=='c'):
                print("==============================================================================================================================")
                print("                Subject                  Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("==============================================================================================================================")
                print("1.)  Engineering Physics Lab                PH3140                  Lab Record -1                    14                15")
                print("2.)  Engineering Physics Lab                PH3140                    Quiz -1                        10                15")
                print("3.)  Professional Communication lab         EG3140                  Lab Record -1                    13                15")
                print("4.)  Professional Communication lab         EG3140                    Quiz -1                        12                15")
                print("5.)  Basic of Computer and C Programming    CS3140                  Lab Record -1                    14                15")
                print("6.)  Basic of Computer and C Programming    CS3140                    Quiz -1                        09                15")
                print("7.)  Personality Development Program        VP3101                  Assignment -1                    30                75")
                print("==============================================================================================================================")
                exam_in()
            elif(a==1 and b=='practical' and c==2 and d=='c'):
                print("==============================================================================================================================")
                print("                Subject                  Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("==============================================================================================================================")
                print("1.)  Engineering Physics Lab                PH3140                  Lab Record -2                    15                15")
                print("2.)  Engineering Physics Lab                PH3140                    Quiz -2                        12                15")
                print("3.)  Professional Communication lab         EG3140                  Lab Record -2                    14                15")
                print("4.)  Professional Communication lab         EG3140                    Quiz -2                        14                15")
                print("5.)  Basic of Computer and C Programming    CS3140                  Lab Record -2                    14                15")
                print("6.)  Basic of Computer and C Programming    CS3140                    Quiz -2                        12                15")
                print("7.)  Personality Development Program        VP3101                  Assignment -2                    32                75")
                print("==============================================================================================================================")
                exam_in()
            elif(a==1 and b=='practical' and c>2 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(a==2 and b=='theory' and c==2 and d=='c'):
                print("\n")
                print("==============================================================================================================================")
                print("                Subject                  Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("==============================================================================================================================")
                print("1.)  Environment Studies                    CY3205                  Sessioonal-2                    21                25")
                print("2.)  Human Values and Ethics                PS3101                  Sessioonal-2                    20                25")
                print("3.)  Graph Theory And Probability           CS3203                  Sessioonal-2                    24                25")
                print("4.)  Advance C Programming                  CS3206                  Sessioonal-2                    20                25")
                print("5.)  HTML5 & CSS                            CS3204                  Sessioonal-2                    22                25")
                print("6.)  Web And Digital Analytics              CS3205                  Sessioonal-2                    22                25")
                print("==============================================================================================================================")
                exam_in()
            elif(a==2 and b=='theory' and c==1 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(a==2 and b=='theory' and c>2 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(a==2 and b=='practical' and c==1 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(a==2 and b=='practical' and c>2 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(a==2 and b=='practical' and c==2 and d=='c'):
                print("\n")
                print("==============================================================================================================================")
                print("                Subject                  Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("==============================================================================================================================")
                print("1.)  Value Added Program                    VP3201                  Sessioonal-2                    24                25")
                print("2.)  HTML5 & CSS                            CS3243                    Quiz -2                       14                15")
                print("3.)  Advance C Programming                  CS3242                    Quiz -2                       14                15")
                print("4.)  Web And Digital Analytics              CS3244                    Quiz -2                       12                15")
                print("==============================================================================================================================")
                exam_in()
            elif(a==3 and b=='theory' and c==1 and d=='c'):
                print("====================================================================================================================================================================")
                print("                Subject                                                        Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("====================================================================================================================================================================")
                print("1.)  Demystifying Artificial Intelligence and Machine Learning                    CS3321                  Mid Sem Exam                    34                40")
                print("2.)  Python Programming                                                           CS3322                  Mid Sem Exam                    38                40")
                print("3.)  Data Structure And Programming                                               CS3301                  Mid Sem Exam                    36                40")
                print("4.)  Discreate Design Structure                                                   CS3302                  Mid Sem Exam                    37                40")
                print("5.)  Database Management System                                                   CS3305                  Mid Sem Exam                    33                40")
                print("6.)  Digital Electronics                                                          EC3306                  Mid Sem Exam                    39                40")
                print("====================================================================================================================================================================")
                exam_in()
            elif(a==3 and b=='theory' and c>1 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(a==3 and b=='practical' and c==1 and d=='c'):
                print("====================================================================================================================================================================")
                print("                Subject                                                        Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("====================================================================================================================================================================")    
                print("1.)  Python Programming Lab                                                       CS3344                     Quiz -1                     19                  20")
                print("2.)  Data Structure Programming Lab                                               CS3340                     Quiz -1                     17                  20")
                print("3.)  Digital Electronics Lab                                                      EC3341                     Quiz -1                     16                  20")
                print("4.)  Oracle/SQL Server Lab                                                        CS3342                     Quiz -1                     16                  20")
                print("5.)  Project Lab 1                                                                CS3346                 Presetation -1                  22                  25")
                print("====================================================================================================================================================================")
                exam_in()
            elif(a==3 and b=='practical' and c==2 and d=='c'):
                print("====================================================================================================================================================================")
                print("                Subject                                                        Subject Code        Sessional/Teacher Assessment     Obtained Marks     Maximum Marks")
                print("====================================================================================================================================================================")
                print("1.)  Python Programming Lab                                                       CS3344                     Quiz -2                     20                  20")
                print("2.)  Data Structure Programming Lab                                               CS3340                     Quiz -2                     20                  20")
                print("3.)  Digital Electronics Lab                                                      EC3341                     Quiz -2                     18                  20")
                print("4.)  Oracle/SQL Server Lab                                                        CS3342                     Quiz -2                     19                  20")
                print("5.)  Project Lab 1                                                                CS3346                 Presetation -2                  24                  25")
                print("====================================================================================================================================================================")
                exam_in()
            elif(a==3 and b=='practical' and c>2 and d=='c'):
                print("\tData Not Found.............")
                exam_in()
            elif(d=='e'):
                exit
            else:
                print("Please Enter Valid Option........")
                exam_in()
        exam_in()
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
btn=Button(a,text="Sessional/TA Marks Statement",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=external).place(x=30,y=100)
btn=Button(a,text="Ext Sem .Exam Apply",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=circular).place(x=77,y=180)
btn=Button(a,text="Summer Sem/Back Paper Apply",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=circular).place(x=25,y=260)
btn=Button(a,text="Online Exam",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=circular).place(x=105,y=340)
btn=Button(a,text="Transaction History",bd=7,bg="white",font=("Arial",15,"bold"),fg="#007FFF",command=circular).place(x=70,y=420)

lb=Label(a,text="Cyborg-ERP : Please Select Menu From Menu Bar.",font=("Arial",14,"bold"),fg="#007FFF").place(x=380,y=100)

a.mainloop()
