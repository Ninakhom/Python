import tkinter
import mysql.connector as mysql
from tkinter import messagebox
import os
frm = tkinter.Tk()
frm.geometry("450x350")
frm.title("Update form")

file=open('info.txt','r')
id=file.read()
# connect database 

con =mysql.connect(host="localhost",user="root",password="",database="python_gui")
custer=con.cursor()

query="select id,f_name,l_name,gender,tel_number from tbl_member where id='"+id+"'"
custer.execute(query)
records =custer.fetchone()

firstname=records[1]
lastnaem=records[2]
gender=records[3]
tel=records[4]


def upData():
    fname=txt_first.get()
    flast=txt_last.get()
    tel=txt_tel.get()
    gender=varGender.get()
    if (gender==1):
        gender='M'
    else:
        gender='F'
    msg=messagebox.askquestion("Confirm","Do you want to update this information")
    if(msg=='yes'):
        query1="update tbl_member set f_name='"+fname+"',l_name='"+flast+"',gender='"+gender+"',tel_number='"+tel+"' where id='"+id+"'"
        custer.execute(query1)
        custer.execute("commit")
        frm.destroy()
        os.system("python Display.py")

lb1 = tkinter.Label(frm,text="Firstname:")
lb1.place(x=50,y=20)
lb1.config(font=('Times New Roman',14,'bold'))

lb2 = tkinter.Label(frm,text="Lastname")
lb2.place(x=50,y=80)
lb2.config(font=('Times New Roman',14,'bold'))

lb3 = tkinter.Label(frm,text="Gender")
lb3.place(x=50,y=140)
lb3.config(font=('Times New Roman',14,'bold'))

lb4 = tkinter.Label(frm,text="Tel")
lb4.place(x=50,y=200)
lb4.config(font=('Times New Roman',14,'bold'))

txt_first= tkinter.Entry(frm)
txt_first.place(x=170,y=20)
txt_first.config(font=('Times New Roman',14,'bold'))

txt_last= tkinter.Entry(frm)
txt_last.place(x=170,y=80)
txt_last.config(font=('Times New Roman',14,'bold'))

txt_tel= tkinter.Entry(frm)
txt_tel.place(x=170,y=200)
txt_tel.config(font=('Times New Roman',14,'bold'))

varGender=tkinter.IntVar()
if(gender=='M'):
    varGender.set(1)

else:
    varGender.set(2)

rd_m=tkinter.Radiobutton(frm,text='Male',variable=varGender,value=1)
rd_m.place(x=170,y=140)
rd_m.config(font=('Times New Roman',14,'bold'))

rd_f=tkinter.Radiobutton(frm,text='Female',variable=varGender,value=2)
rd_f.place(x=270,y=140)
rd_f.config(font=('Times New Roman',14,'bold'))

btn_update=tkinter.Button(frm,text="Update",width=10,command=upData)
btn_update.place(x=80,y=260)
btn_update.config(font=('Times New Roman',14,'bold'))

btn_cancel=tkinter.Button(frm,text="Cancel",width=10)
btn_cancel.place(x=260,y=260)
btn_cancel.config(font=('Times New Roman',14,'bold'))

txt_first.insert(1, firstname)
txt_last.insert(2,lastnaem)
txt_tel.insert(3,tel)

frm.mainloop()
