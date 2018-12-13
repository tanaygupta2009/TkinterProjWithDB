from Tkinter import *
from tkMessageBox import *
from sqlite3 import *
import re
con=Connection('dbproj')
cur=con.cursor()
imageins=Tk()
img=PhotoImage(file='log.gif')
lb=Label(imageins,image=img).pack()
def fun():
    imageins.destroy()
Button(imageins,text='Enter to Programm',command=fun).pack()
imageins.mainloop()
login=Tk()
login.title('Login Page')
Label(login,text='Login / Signup Page',font='comic 40 bold',fg='Steel Blue',bd=10).grid(row=0,column=0,columnspan=2)
Label(login,text='Username',font='comic 10 bold').grid(row=1,column=0)
user1=Entry(login)
user1.grid(row=1,column=1)
Label(login,text='Password',font='comic 10 bold').grid(row=2,column=0)
pass1=Entry(login)
pass1.grid(row=2,column=1)
cur.execute("create table if not exists login(Username varchar(20),FirstName varchar(20),LastName varchar(20),password varchar(20),UniqueQue varchar(60),UniqueAns varchar(20),EMail varchar(30),PRIMARY KEY (Username))")
def signup():
    signup=Tk()
    Label(signup,text='Signup',font='comic 30 bold',fg='Steel Blue',bd=10).grid(row=0,column=0,columnspan=2)
    Label(signup,text='Username',font='comic 10').grid(row=1,column=0)
    signuser=Entry(signup,width=20,bd=3)
    signuser.grid(row=1,column=1)
    Label(signup,text='First Name',font='comic 10').grid(row=2,column=0)
    signname=Entry(signup,width=20,bd=3)
    signname.grid(row=2,column=1)
    Label(signup,text='Last Name',font='comic 10').grid(row=3,column=0)
    signLname=Entry(signup,width=20,bd=3)
    signLname.grid(row=3,column=1)
    Label(signup,text='Password',font='comic 10').grid(row=4,column=0)
    signpass=Entry(signup,width=20,bd=3)
    signpass.grid(row=4,column=1)
    Label(signup,text='Unique Question',font='comic 10').grid(row=5,column=0)
    signque=Entry(signup,width=20,bd=3)
    signque.grid(row=5,column=1)
    Label(signup,text='Unique Answer',font='comic 10').grid(row=6,column=0)
    signans=Entry(signup,width=20,bd=3)
    signans.grid(row=6,column=1)
    Label(signup,text='E-Mail',font='comic 10').grid(row=7,column=0)
    signmail=Entry(signup,width=20,bd=3)
    signmail.grid(row=7,column=1)
    def validate(email): 
        match=re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",email)
        if match:
            return 1
        else:
            return 0
    def insert():
        Username=(signuser.get())
        Fname=(signname.get())
        Lname=(signLname.get())
        Password=(signpass.get())
        UniqueQue=(signque.get())
        UniqueAns=(signque.get())
        Email=(signmail.get())
        k=validate(signmail.get())
        if Username=='' or Fname=='' or Lname=='' or Password=='' or UniqueQue=='' or UniqueAns=='' or Email=='':
            showerror('error','Some fields are empty')
        else:
            if k==1:
                cur.execute("select Username from login where Username=?",(Username,))
                data=cur.fetchall()
                if not data:
                    cur.execute("insert into login values(?,?,?,?,?,?,?)",(Username,Fname,Lname,Password,UniqueQue,UniqueAns,Email))
                    con.commit()
                    showinfo('Success','Successfully signed up')
                else:
                    showerror('error','Username already exist, try another one')
            if k==0:
                showerror('error','Invalid Email syntax')
            
    Button(signup,text='SignUp',command=insert).grid(row=8,column=0)
    def exit7():
        signup.destroy()
    Button(signup,text='Exit',command=exit7).grid(row=8,column=1)
    signup.mainloop()
def logon():
    data2=cur.execute("select Username from login where Username=? and password=?",(user1.get(),pass1.get(),)).fetchall()
    if not data2:
        showerror('error','Username or password incorrect / Username does not exist')
    else:
        con2=Connection('student')
        cur2=con2.cursor()
        cur2.execute("create table if not exists student(EnrollNumber varchar(20),Name varchar(20),DOB date,Address varchar(40),Phone number(15),PRIMARY KEY (EnrollNumber))")
        cur2.execute("create table if not exists marks(EnrollNumber varchar(20),Math number(20),English number(20),Science number(20),FOREIGN KEY(EnrollNumber) REFERENCES student(EnrollNumber))")
        cur2.execute("create table if not exists result(EnrollNumber varchar(20),Result number(20),FOREIGN KEY (EnrollNumber) REFERENCES student(EnrollNumber))")
        root=Tk()
        root.title('Student record keeper')
        Label(root,text='Student record Keeping System',font='comic 20 bold',fg='Steel Blue',bd=10).grid(row=0,column=0,columnspan=2)
        global Date
        def EntryIns():
            entry=Tk()
            Label(entry,text='Student Data Entry',font='comic 30 bold',fg='Steel Blue',bd=10).grid(row=0,column=0,columnspan=4)
            Label(entry,text='EnRollment Number: ').grid(row=1,column=0)                 
            enEnroll=Entry(entry)
            enEnroll.grid(row=1,column=2)
            Label(entry,text='Name: ').grid(row=2,column=0)
            enName=Entry(entry)
            enName.grid(row=2,column=2)
            Day=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
            Month=['January','February','March','April','May','June','July','August','September','October','November','December']
            Year=['1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
            DayVar=StringVar(entry)
            DayVar.set(Day[0])
            MonthVar=StringVar(entry)
            MonthVar.set(Month[0])
            YearVar=StringVar(entry)
            YearVar.set(Year[0])
            DayDrop=OptionMenu(entry,DayVar,*Day)
            DayDrop.grid(row=3,column=1)
            MonthDrop=OptionMenu(entry,MonthVar,*Month)
            MonthDrop.grid(row=3,column=2)
            YearDrop=OptionMenu(entry,YearVar,*Year)
            YearDrop.grid(row=3,column=3)
            Label(entry,text='Date Of Birth: ').grid(row=3,column=0)
            Label(entry,text='Address:').grid(row=4,column=0)
            enAddress=Entry(entry)
            enAddress.grid(row=4,column=2)
            Label(entry,text='Phone Number: ').grid(row=5,column=0)
            enPhone=Entry(entry)
            enPhone.grid(row=5,column=2)
            def insert():
                Date=DayVar.get()+"-"+MonthVar.get()+"-"+YearVar.get()
                Enroll=enEnroll.get()
                Name=enName.get()
                Address=enAddress.get()
                Phone=enPhone.get()
                if Enroll=='' or Name=='' or Address=='' or Phone=='':
                    showerror('error','Some fields are empty')
                cur2.execute("select EnrollNumber from student where EnrollNumber=?",(Enroll,))
                data3=cur2.fetchall()
                if not data3:
                    if(len(Phone)==10):
                        cur2.execute("insert into student values(?,?,?,?,?)",(Enroll,Name,Date,Address,Phone),)
                        con2.commit()
                        showinfo('Success','Data inserted successfully')
                    else:
                        showerror('error','invalid phone number, it must have 10 digits')
                else:
                    showerror('error','Enrollment number already taken, try another')
            def exit2():
                entry.destroy()
            def Reseting():
                enEnroll.delete(0,END)
                enName.delete(0,END)
                enAddress.delete(0,END)
                enPhone.delete(0,END)
            Button(entry,text='Insert',command=insert,width=10,height=2).grid(row=6,column=0)
            Button(entry,text='Reset',command=Reseting,width=10,height=2).grid(row=6,column=1)
            Button(entry,text='Exit',command=exit2,width=10,height=2).grid(row=6,column=3)
            entry.mainloop()
        def exit1():
            root.destroy()
            entry.destroy()
            info.destroy()
            exam.destroy()
            showinfo('Success','You have been signed out')
        def Displayinfo():
            info=Tk()
            Label(info,text='Student Info Display',font='comic 30 bold',fg='Steel Blue',bd=10).grid(row=0,column=0,columnspan=5)
            Label(info,text='Enrollment No.',font='comic 20 bold',bd=10).grid(row=1,column=0)
            Label(info,text='Name',font='comic 20 bold',bd=10).grid(row=1,column=1)
            Label(info,text='Date of Birth',font='comic 20 bold',bd=10).grid(row=1,column=2)
            Label(info,text='Address',font='comic 20 bold',bd=10).grid(row=1,column=3)
            Label(info,text='Phone Number',font='comic 20 bold',bd=10).grid(row=1,column=4)
            cur2.execute("select EnrollNumber from student")
            inEnroll=cur2.fetchall()
            a=[]
            a=inEnroll
            i=0
            r=2
            while(i<len(a)):
                Label(info,text=a[i],font='comic 10 bold').grid(row=r,column=0)
                i=i+1
                r=r+1
            cur2.execute("select Name from student")
            inName=cur2.fetchall()
            b=[]
            b=inName
            i=0
            r=2
            while(i<len(b)):
                Label(info,text=b[i],font='comic 10 bold').grid(row=r,column=1)
                i=i+1
                r=r+1
            cur2.execute("select DOB from student")
            inDate=cur2.fetchall()
            c=[]
            c=inDate
            i=0
            r=2
            while(i<len(c)):
                Label(info,text=c[i],font='comic 10 bold').grid(row=r,column=2)
                i=i+1
                r=r+1
            cur2.execute("select Address from student")
            inAddress=cur2.fetchall()
            d=[]
            d=inAddress
            i=0
            r=2
            while(i<len(d)):
                Label(info,text=d[i],font='comic 10 bold').grid(row=r,column=3)
                i=i+1
                r=r+1
            cur2.execute("select Phone from student")
            inPhone=cur2.fetchall()
            e=[]
            e=inPhone
            i=0
            r=2
            while(i<len(e)):
                Label(info,text=e[i],font='comic 10 bold').grid(row=r,column=4)
                i=i+1
                r=r+1
            def exit3():
                info.destroy()
            Button(info,text='Exit',command=exit3,width=10,height=2).grid(row=1,column=5)
            info.mainloop()
        def ExamInput():
            exam=Tk()
            Label(exam,text='Enter Marks obtained By a Student',fg='Steel Blue',font='comic 20 bold').grid(row=0,column=0,columnspan=2)
            Label(exam,text='EnRollment Number: ').grid(row=1,column=0)
            exEnroll=Entry(exam)
            exEnroll.grid(row=1,column=1)
            Label(exam,text='Marks obtained in Mathematics : ').grid(row=2,column=0)
            exMath=Entry(exam)
            exMath.grid(row=2,column=1)
            Label(exam,text='Marks obtained in English : ').grid(row=3,column=0)
            exEng=Entry(exam)
            exEng.grid(row=3,column=1)
            Label(exam,text='Marks obtained in Science : ').grid(row=4,column=0)
            exSci=Entry(exam)
            exSci.grid(row=4,column=1)
            def insres():
                Enroll=exEnroll.get()
                Math=exMath.get()
                Eng=exEng.get()
                Sci=exSci.get()
                if Enroll=='' or Math=='' or Eng=='' or Sci=='':
                    showerror('error','Some fields are empty')
                if int(Math)>100 or int(Eng)>100 or int(Sci)>100:
                    showerror('error','Invalid marks,marks cannot be greater than 100!')
                else:
                    cur2.execute("select EnrollNumber from student where EnrollNumber=?",(Enroll,))
                    data4=cur2.fetchall()
                    if not data4:
                        showerror('error','Username Doesnt Exist')
                    else:
                        cur2.execute("insert into marks values(?,?,?,?)",(Enroll,Math,Eng,Sci),)
                        showinfo('Success','Data Entered Successfully')
                    result=int(Math)+int(Eng)+int(Sci)
                    Percentage=result/3
                    cur2.execute("insert into result values(?,?)",(Enroll,Percentage),)
                    con2.commit()
            def exit5():
                exam.destroy()
            Button(exam,text='Exit',command=exit5,width=10,height=2).grid(row=6,column=0,columnspan=2)
            Button(exam,text='Enter',command=insres,width=10,height=2).grid(row=5,column=0,columnspan=2)
            exam.mainloop()
        def ExamRes():
            result=Tk()
            Label(result,text='Exam Result',fg='Steel Blue',font='comic 30 bold').grid(row=0,column=0,columnspan=3)
            Label(result,text='EnRollment Number',font='comic 20 bold',bd=10).grid(row=1,column=0)
            Label(result,text='Result in Percentage',font='comic 20 bold',bd=10).grid(row=1,column=1)
            cur2.execute("select EnrollNumber from result")
            resEnroll=cur2.fetchall()
            q=[]
            q=resEnroll
            i=0
            r=2
            while(i<len(q)):
                Label(result,text=q[i],font='comic 10 bold').grid(row=r,column=0)
                i=i+1
                r=r+1
            cur2.execute("select Result from result")
            resResult=cur2.fetchall()
            w=[]
            w=resResult
            i=0
            r=2
            while(i<len(w)):
                Label(result,text=w[i],font='comic 10 bold').grid(row=r,column=1)
                i=i+1
                r=r+1
            def exit6():
                result.destroy()
            Button(result,text='Exit',command=exit6,width=10,height=2).grid(row=1,column=2)
            result.mainloop()
        Button(root,text='New Entry',command=EntryIns,width=10,height=2).grid(row=1,column=0)
        Button(root,text='Show Info',command=Displayinfo,width=10,height=2).grid(row=2,column=0)
        Button(root,text='SignOut',command=exit1,width=10,height=2).grid(row=3,column=0,columnspan=2)
        Button(root,text='Marks Entry',command=ExamInput,width=10,height=2).grid(row=1,column=1)
        Button(root,text='Show Result',command=ExamRes,width=10,height=2).grid(row=2,column=1)
        root.mainloop()

Button(login,text='Login',command=logon).grid(row=3,column=0)
Button(login,text='Signup',command=signup).grid(row=3,column=1)
login.mainloop()
        
    
 
