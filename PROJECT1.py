#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import*
import tkinter as tk
from tkinter import ttk 
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="I@mSuneela143",database="project")
cursor=con.cursor()
#cursor.execute("create table open_hours ( UID INT AUTO_INCREMENT PRIMARY KEY,Supervisor_name  varchar(255),openhours varchar(255) )")
#cursor.execute("create table students_details( Reg_no INT AUTO_INCREMENT PRIMARY KEY, first_name varchar(255),last_name varchar(255),specialization varchar(255), phn_no int(10),emailid varchar(255))")
#cursor.execute("create table super_details(UID INT AUTO_INCREMENT PRIMARY KEY,first_name varchar(255),last_name varchar(255),specialization varchar(255), phn_no int(10),emailid varchar(255))")

sql=("insert into open_hours(Supervisor_name,openhours) values(%s,%s)")
val=[('Bhupinder Kaur','10 to 12, 3 to 4'),('Ramandeep Singh','11 to 12, 4 to 5'),('Amandeep Kaur','9 to 10, 2 to 3'),('Nahida Nazir','9 to 11, 3 to 5'),('Roopam','10 to 11, 1to 3'),]
cursor.executemany(sql,val)
con.commit

cursor.execute("select * from open_hours")
result=cursor.fetchall()
for i in result:
    print(i)

sql1=("insert into students_details(first_name,last_name,specialization,phn_no,emailid) values(%s,%s,%s,%s,%s)")
val1=[('Maddineni','Suneela','CSE',63027975,'suneela@gmail.com'),('Pusuluri','Srilakshmi','CSE',6304083,'lakshmi@gmail.com'),('Bhaskara','Keerthi','CSE',12345690,'keerthi@gmail.com'),]
cursor.executemany(sql1,val1)
con.commit

cursor.execute("select * from students_details")
result1=cursor.fetchall()
for i in result1:
    print(i)
    
    
sql2=("insert into super_details(first_name,last_name,specialization,phn_no,emailid) values(%s,%s,%s,%s,%s)")
val2=[('Bhupinder','Kaur','Python',63027975,'bhupinder@gmail.com'),('Ramandeep','Singh','English',6304083,'ramandeep@gmail.com'),('Amandeep','Kaur','Data structures',12345690,'amandeep@gmail.com'),('Nahida','Nazir','DBMS',123456,'nahida@gmail.com'),('Roopam','','Software engineering',56789876,'roopam@gmail.com'),]
cursor.executemany(sql2,val2)
con.commit

cursor.execute("select * from super_details")
result1=cursor.fetchall()
for i in result1:
    print(i)



#cursor.execute("create database project")
#cursor.execute("create table ")
root=Tk()
root.title("Main page")
#============================       Select students  ===========================
def select_students():
    root=Tk()
    root.geometry("600x600")
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',value=i)
    
        
    lf=LabelFrame(root,text="Students",bg="darkseagreen",fg="deeppink")
    #==========================================
    #       tree view
    trv=ttk.Treeview(lf, column=(1,2,3,4,5,6), show="headings",height="5") 
    trv.pack() 
    trv.heading(1,text="Registration number")
    trv.heading(2,text="First Name")
    trv.heading(3,text="Last Name") 
    trv.heading(4,text="Specialization") 
    trv.heading(5,text="Mobile number")
    trv.heading(6,text="Email ID")
    #===========================================
    cursor.execute("select Reg_no,first_name,last_name,specialization,phn_no,emailid from students_details")
    rows=cursor.fetchall()
    update(rows)
    lf.pack(fill="both",expand="yes",padx=20,pady=20)
    def select():
        root=Tk()
        f=Frame(root,height=250,width=500,bg="gold")
        f.pack()
        b=Button(f,bitmap="hourglass",bg="springgreen",fg="black")
        b.place(x=230,y=80)
        l=Label(f,text="Successfully Selected",bg="darkolivegreen1",fg="skyblue1")
        l.place(x=180,y=110)
        root.mainloop()
        
    btn=Button(lf,text="Select",bg="pink",fg="gray",command=select)
    btn.pack()
    root.mainloop()





#============================     Request for supervisor   ========================
def req_for_super():
    root=Tk()
    root.geometry("600x600+200+200")
    l1=Label(root,text="Request for supervisor",width=30,bg="black",fg="white")
    l1.pack()
  
    def update(rows): 
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',value=i)
    
    lf=LabelFrame(root,text="Supervisors",bg="tan2",fg="deeppink")
    #==========================================
    #       tree view
    trv=ttk.Treeview(lf, column=(1,2,3,4,5,6), show="headings",height="5") 
    trv.pack() 
    trv.heading(1,text="UID")
    trv.heading(2,text="First Name")
    trv.heading(3,text="Last Name") 
    trv.heading(4,text="Specialization") 
    trv.heading(5,text="Mobile number")
    trv.heading(6,text="Email ID")
    #===========================================
    cursor.execute("select UID,first_name,last_name,specialization,phn_no,emailid from super_details")
    rows=cursor.fetchall()
    update(rows)
    def request():
        root=Tk()
        f=Frame(root,height=250,width=500,bg="gold")
        f.pack()
        b=Button(f,bitmap="hourglass",bg="springgreen",fg="black")
        b.place(x=230,y=80)
        l=Label(f,text="Successfully Requested",bg="springgreen",fg="black")
        l.place(x=180,y=110)
        root.mainloop()

        
    lf.pack(fill="both", expand="yes", padx=20, pady=20) 
    btn=Button(lf,text="Request",bg="blue",fg="pink",command=request)
    btn.pack()
    
    
    root.mainloop()




#=============================      Open hours       ============================
def open_hours():
    root=Tk()
    root.geometry("600x600+200+200") 
    def update(rows): 
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',value=i)
    wrapper1=LabelFrame(root,text="OpenHours",bg="mediumorchid",fg="purple")
    trv=ttk.Treeview(wrapper1, column=(1,2,3), show="headings",height="5") 
    trv.pack()
    trv.heading(1,text="UID")
    trv.heading(2,text="Supervisor Name") 
    trv.heading(3,tex="Open hours") 
    query="select UID,Supervisor_name,openhours from open_hours"
    cursor.execute(query) 
    rows=cursor.fetchall() 
    update(rows) 




    wrapper1.pack(fill="both", expand="yes", padx=20, pady=20) 
    root.mainloop()

######################################      Register  #############################################
def register():
    root=Tk()
    f=Frame(root,height=250,width=500,bg="blue")
    f.pack()
    b=Button(f,bitmap="hourglass",bg="yellow",fg="black")
    b.place(x=230,y=80)
    l=Label(f,text="Successfully Registered",bg="yellow",fg="black")
    l.place(x=180,y=110)
    root.mainloop()

#######################################   Login now    ############################################
def login_now():
    root=Tk()
    f=Frame(root,height=250,width=500,bg="blue")
    f.pack()
    b=Button(f,bitmap="hourglass",bg="yellow",fg="black")
    b.place(x=230,y=80)
    l=Label(f,text="Successfully Logged in",bg="yellow",fg="black")
    l.place(x=180,y=110)
    root.mainloop()

######################################       New User Student    #############################################
def new_user_student():
    root=Tk()
    root.geometry("600x600")
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',value=i)
        
        
    ''''  
    def search():
        e2=q.get()
        query="select first_name,last_name,specialization,phn_no,emailid from students_details where first_name LIKE '%"+e2+"%' "
        cursor.execute(query)
        update (rows)
    '''
        
        
    lf=LabelFrame(root,text="Students",bg="navy",fg="deeppink")
    #==========================================
    #       tree view
    trv=ttk.Treeview(lf, column=(1,2,3,4,5,6), show="headings",height="5") 
    trv.pack() 
    trv.heading(1,text="Registration number")
    trv.heading(2,text="First Name")
    trv.heading(3,text="Last Name") 
    trv.heading(4,text="Specialization") 
    trv.heading(5,text="Mobile number")
    trv.heading(6,text="Email ID")
    #===========================================
    cursor.execute("select Reg_no,first_name,last_name,specialization,phn_no,emailid from students_details")
    rows=cursor.fetchall()
    update(rows)
    
    q=StringVar()
    l1=Label(root,text="New User Student",width=30,bg="black",fg="white")
    l1.pack()
    f=Frame(root,height=400,width=500,bg="olivedrab2")
    f.pack() 
    l2=Label(f,text=" First Name",bg="cyan")
    l2.place(x=50,y=50)
   
    e1=Entry(f,width=20,bg="blue",fg="yellow",textvariable=q)
    e1.place(x=200,y=50)
    l3=Label(f,text="Last Name",fg="black",bg="pink")
    l3.place(x=50,y=100)
    e2=Entry(f,width=20,bg="blue",fg="yellow")
    e2.place(x=200,y=100)
    l4=Label(f,text="Specialization",fg="black",bg="purple")
    l4.place(x=50,y=150)
    e3=Entry(f,width=20,bg="blue",fg="yellow")
    e3.place(x=200,y=150)
    l5=Label(f,text="Mobile number",fg="black",bg="yellow")
    l5.place(x=50,y=200)
    e4=Entry(f,width=20,bg="blue",fg="yellow")
    e4.place(x=200,y=200)
    l6=Label(f,text="Email Address",fg="black",bg="red")
    l6.place(x=50,y=250)
    e5=Entry(f,width=20,bg="blue",fg="yellow")
    e5.place(x=200,y=250)
    #b=Button(f,text="Show",relief=GROOVE,fg="peachpuff",bg="blue",command=search)
   # b.place(x=100,y=380)
    b1=Button(f,text="Register",relief=RIDGE,fg="blue",bg="peachpuff",command=register)
    b1.place(x=100,y=300)
    lf.pack(fill="both",expand="yes",padx=20,pady=20)
    root.mainloop()

#####################################       Student login    ############################################
def student_login():
    root=Tk()
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',value=i)
        
        
    ''''  
    def search():
        e2=q.get()
        query="select first_name,last_name,specialization,phn_no,emailid from students_details where first_name LIKE '%"+e2+"%' "
        cursor.execute(query)
        update (rows)
    '''
        
        
    lf=LabelFrame(root,text="Students",bg="darkgreen",fg="ivory2")
    #==========================================
    #       tree view
    trv=ttk.Treeview(lf, column=(1,2,3,4,5,6), show="headings",height="5") 
    trv.pack() 
    trv.heading(1,text="Registration number")
    trv.heading(2,text="First Name")
    trv.heading(3,text="Last Name") 
    trv.heading(4,text="Specialization") 
    trv.heading(5,text="Mobile number")
    trv.heading(6,text="Email ID")
    #===========================================
    cursor.execute("select Reg_no,first_name,last_name,specialization,phn_no,emailid from students_details")
    rows=cursor.fetchall()
    update(rows)
    l=Label(root,text="Student Login",bg="black",fg="gray")
    l.pack()
    f=Frame(root,height=200,width=500,bg="maroon1")
    f.pack()
    l1=Label(f,text="User name",bg="purple",fg="cyan")
    l1.place(x=50,y=50)
    e1=Entry(f,width=20,bg="cyan",fg="purple")
    e1.place(x=150,y=50)
    l2=Label(f,text="Password",bg="yellow",fg="blue")
    l2.place(x=50,y=100)
    e2=Entry(f,width=20,show="*",bg="blue",fg="yellow")
    e2.place(x=150,y=100)
    b1=Button(f,text="New User",relief=GROOVE,bg="pink",fg="white",command=new_user_student)
    b1.place(x=125,y=170)
    b2=Button(f,text="Login now",relief=RIDGE,bg="orchid1",fg="blue",command=login_now)
    b2.place(x=125,y=130)
    lf.pack(fill="both",expand="yes",padx=20,pady=20)
    root.mainloop()
##########################################    Student    #########################################
def student():
    root=Tk()
    l1=Label(root,text="Student",width=20,bg="black",fg="white")
    l1.pack()
    f=Frame(root,height=200,width=500,bg="purple")
    f.pack()        
    b1=Button(f,text="Login",bg="pink",fg="black",relief=GROOVE,command=student_login)
    b1.place(x=9,y=90)
    b1=Button(f,text="New User",bg='cyan',fg="black",relief=GROOVE,command=new_user_student)
    b1.place(x=103,y=90)
    b1=Button(f,text="Request for supervisor",bg="yellow",fg="black",relief=GROOVE,command=req_for_super)
    b1.place(x=200,y=90)
    root.mainloop()
######################################  New Supervisor Register  #############################################
def new_user_supervisor():
    root=Tk()
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',value=i)
        
        
    ''''  
    def search():
        e2=q.get()
        query="select first_name,last_name,specialization,phn_no,emailid from students_details where first_name LIKE '%"+e2+"%' "
        cursor.execute(query)
        update (rows)
    '''
        
        
    lf=LabelFrame(root,text="Supervisors",bg="magenta4",fg="deeppink")
    #==========================================
    #       tree view
    trv=ttk.Treeview(lf, column=(1,2,3,4,5,6), show="headings",height="5") 
    trv.pack() 
    trv.heading(1,text="UID")
    trv.heading(2,text="First Name")
    trv.heading(3,text="Last Name") 
    trv.heading(4,text="Specialization") 
    trv.heading(5,text="Mobile number")
    trv.heading(6,text="Email ID")
    #===========================================
    cursor.execute("select UID,first_name,last_name,specialization,phn_no,emailid from super_details")
    rows=cursor.fetchall()
    update(rows)
    l1=Label(root,text="New User Supervisor",width=30,bg="black",fg="white")
    l1.pack()
    f=Frame(root,height=400,width=500,bg="salmon")
    f.pack() 
    l2=Label(f,text=" First Name",bg="yellow",fg="purple")
    l2.place(x=50,y=50)
    e1=Entry(f,width=20,bg="blue",fg="yellow")
    e1.place(x=200,y=50)
    l3=Label(f,text="Last name",fg="black",bg="cyan")
    l3.place(x=50,y=100)
    e2=Entry(f,width=20,bg="blue",fg="yellow")
    e2.place(x=200,y=100)
    l4=Label(f,text="Specialization",fg="black",bg="purple")
    l4.place(x=50,y=150)
    e3=Entry(f,width=20,bg="blue",fg="yellow")
    e3.place(x=200,y=150)
    l5=Label(f,text="Mobile number",fg="black",bg="pink")
    l5.place(x=50,y=200)
    e4=Entry(f,width=20,bg="blue",fg="yellow")
    e4.place(x=200,y=200)
    l6=Label(f,text="Email Address",fg="black",bg="green")
    l6.place(x=50,y=250)
    e5=Entry(f,width=20,bg="blue",fg="yellow")
    e5.place(x=200,y=250)
    b1=Button(f,text="Register",relief=RIDGE,fg="blue",bg="orange",command=register)
    b1.place(x=100,y=300)
    lf.pack(fill="both",expand="yes",padx=20,pady=20)
    root.mainloop()
##########################################     Supervisor  login  #########################################
def supervisor_login():
    root=Tk()
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('','end',value=i)
        
        
    ''''  
    def search():
        e2=q.get()
        query="select first_name,last_name,specialization,phn_no,emailid from students_details where first_name LIKE '%"+e2+"%' "
        cursor.execute(query)
        update (rows)
    '''
        
        
    lf=LabelFrame(root,text="Supervisors",bg="slateblue3",fg="red")
    #==========================================
    #       tree view
    trv=ttk.Treeview(lf, column=(1,2,3,4,5,6), show="headings",height="5") 
    trv.pack() 
    trv.heading(1,text="UID")
    trv.heading(2,text="First Name")
    trv.heading(3,text="Last Name") 
    trv.heading(4,text="Specialization") 
    trv.heading(5,text="Mobile number")
    trv.heading(6,text="Email ID")
    #===========================================
    cursor.execute("select UID,first_name,last_name,specialization,phn_no,emailid from super_details")
    rows=cursor.fetchall()
    update(rows)
    l=Label(root,text="Supervisor Login Page",bg="black",fg="gray")
    l.pack()
    f=Frame(root,height=200,width=500,bg="cadetblue4")
    f.pack()
    l1=Label(f,text="User name",bg="purple",fg="cyan")
    l1.place(x=50,y=50)
    e1=Entry(f,width=20,bg="cyan",fg="purple")
    e1.place(x=150,y=50)
    l2=Label(f,text="Password",bg="yellow",fg="blue")
    l2.place(x=50,y=100)
    e2=Entry(f,width=20,show="*",bg="blue",fg="yellow")
    e2.place(x=150,y=100)
    b1=Button(f,text="New User",relief=GROOVE,bg="pink",fg="white",command=new_user_supervisor)
    b1.place(x=125,y=170)
    b2=Button(f,text="Login now",relief=RIDGE,bg="orange",fg="blue",command=login_now)
    b2.place(x=125,y=130)
    lf.pack(fill="both",expand="yes",padx=20,pady=20)
    root.mainloop()
#########################################      Supervisor   ##########################################
def supervisor():
    root=Tk()
    l=Label(root,text="Supervisor",bg="black",fg="gray")
    l.pack()
    f=Frame(root,height=400,width=500,bg="yellow")
    f.pack()
    b1=Button(f,text="LOGIN",relief=GROOVE,fg="purple",bg="cyan",command=supervisor_login)
    b1.place(x=50,y=50)
    b2=Button(f,text="New User Supervisor",relief=GROOVE,bg="purple",fg="yellow",command=new_user_supervisor)
    b2.place(x=150,y=50)
    b3=Button(f,text="Open hours",relief=GROOVE,bg="blue",fg="white",command=open_hours)
    b3.place(x=50,y=100)
    b4=Button(f,text="Select Students",relief=GROOVE,bg="gray",fg="pink",command=select_students)
    b4.place(x=150,y=100)

###################################################################################
L=Label(root,text="Who are you?",fg="white",bg="black")
L.pack()
f=Frame(root,height=250,width=500,bg="deepskyblue")
f.pack()
b1=Button(f,text="Student",bg="green",fg="yellow",relief=RIDGE,command=student)
b1.place(x=120,y=110)
b2=Button(f,text="Supervisor",bg="yellow",fg="red",relief=RIDGE,command=supervisor)
b2.place(x=320,y=110)
root.mainloop()


# In[ ]:




