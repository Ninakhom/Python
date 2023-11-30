import tkinter
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
import subprocess
import os

con=mysql.connect(host="localhost",user="root",password="",database="python_gui")
custor=con.cursor()

def login():
    user=uname.get()
    password=passs.get()

    sql="select * from tbl_member where username=%s and passwd=%s"
    custor.execute(sql,(user,password))
    myresult=custor.fetchone()
    

    if myresult is None:
        Messagebox.showinfo("Error","Sorry your username or password incorect")
    else:
        # import Day1
        frm1.destroy()
        os.system("python Day1.py")
        
def Showpassword():
    if (v1.get()==1):
        passs.config(show='')
    else:
        passs.config(show='*')
        
        
        

        
frm1=tkinter.Tk()
frm1.geometry('500x400')
frm1.title('Login')

label1=tkinter.Label(frm1,text='Username :')
label1.place(x=70,y=60)
label1.config(font=('Times New Roman',15))

uname=tkinter.Entry(frm1,width=24)
uname.place(x=180,y=60)
uname.config(font=('Times New Roman',15))

label2=tkinter.Label(frm1,text='Password :')
label2.place(x=70,y=130)
label2.config(font=('Times New Roman',15))

passs=tkinter.Entry(frm1,width=24,show="*",)
passs.place(x=180,y=130)
passs.config(font=('Times New Roman',15))

v1=tkinter.IntVar()
cb_pass=tkinter.Checkbutton(frm1,text="Show Password", variable=v1, onvalue=1, offvalue=0 ,command=Showpassword)
cb_pass.place(x=180,y=160)

btnlog=tkinter.Button(frm1,text="Login",width=15,command=login)
btnlog.place(x=70,y=180)
btnlog.config(font=('Times New Roman',15))

btncan=tkinter.Button(frm1,text="Cancel",width=15,command=quit)
btncan.place(x=250,y=180)
btncan.config(font=('Times New Roman',15))

frm1.mainloop()