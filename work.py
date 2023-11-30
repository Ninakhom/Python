import tkinter 
from tkinter import ttk
from tkcalendar import Calendar
import mysql.connector as mysql
from tkinter import messagebox


frm=tkinter.Tk()
frm.geometry("1000x600")

con = mysql.connect(host="localhost",user="root",password="", database="python_gui")
custor=con.cursor()

def save():
    StID=txtstID.get()
    Name=txtFn.get()
    birth=cal.get_date()
    gender=varGender.get()
    year=varYear.get()
    maj=val_major.get()

    robot=val_robot.get()
    eng=val_eng.get()
    sta=val_startup.get()
    sup=val_support.get()
    iot=val_iot.get()
    print(birth)
#convert
    robot_value = 'yes' if robot else 'no'
    eng_value = 'yes' if eng else 'no'
    sta_value = 'yes' if sta else 'no'
    sup_value = 'yes' if sup else 'no'
    iot_value = 'yes' if iot else 'no'
    
        
    #check student ID
    query="select * from tbl_club where student_id ='"+StID+"'"
    custor.execute(query)
    record=custor.fetchall()
    
    if len(record)!=0:
        messagebox.showinfo("Info","This Id already have") 
    else:
        query = "INSERT INTO tbl_club (student_id, name, gender, birth, year,major,robot, english, startup, support, iot) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)"
        values = (StID, Name, gender,birth ,year,maj,robot_value, eng_value, sta_value, sup_value, iot_value)
        custor.execute(query, values)
        con.commit()
        messagebox.showinfo("Success", "Data saved successfully")
    

varGender=tkinter.IntVar()
varGender.set(1)

varYear=tkinter.IntVar()
varYear.set(1)

lbID=tkinter.Label(frm,text="Student_id:")
lbID.place(x="30",y="10")
lbID.config(font=('Times New Roman',16))

txtstID=tkinter.Entry(frm,)
txtstID.place(x=150,y=10)
txtstID.config(font=('Times New Roman',16))

lbFn=tkinter.Label(frm,text="Fullname: ")
lbFn.place(x=30,y=80)
lbFn.config(font=('Times New Roman',16))

txtFn=tkinter.Entry(frm,)
txtFn.place(x=150,y=80)
txtFn.config(font=('Times New Roman',16))

lbFn=tkinter.Label(frm,text="Gender: ")
lbFn.place(x=30,y=150)
lbFn.config(font=('Times New Roman',16))

rdM=tkinter.Radiobutton(frm,text="Male",variable=varGender,value=1)
rdM.place(x=150,y=150)
rdM.config(font=('Times New Roman',16))

rdF=tkinter.Radiobutton(frm,text="Female",variable=varGender,value=2)
rdF.place(x=250,y=150)
rdF.config(font=("Times New Roman",16))

lbFn=tkinter.Label(frm,text="Year: ")
lbFn.place(x=30,y=220)
lbFn.config(font=('Times New Roman',16))

rd1=tkinter.Radiobutton(frm,text="1",variable=varYear,value=1)
rd1.place(x=150,y=220)
rd1.config(font=('Times New Roman',16))

rd2=tkinter.Radiobutton(frm,text="2",variable=varYear,value=2)
rd2.place(x=200,y=220)
rd2.config(font=("Times New Roman",16))

rd3=tkinter.Radiobutton(frm,text="3",variable=varYear,value=3)
rd3.place(x=250,y=220)
rd3.config(font=('Times New Roman',16))

rd4=tkinter.Radiobutton(frm,text="4",variable=varYear,value=4)
rd4.place(x=300,y=220)
rd4.config(font=("Times New Roman",16))

lbM = tkinter.Label(frm,text="Major: ")
lbM.place(x=30,y=290)
lbM.config(font=("Times New Roman",16))

val_major = tkinter.StringVar()
cbb=ttk.Combobox(frm,textvariable=val_major,state='readonly')
cbb.place(x=150,y=290)
cbb.config(font=("Times New Roman",16))
cbb['values'] = ('Programming', 'Network', 'Management', 'Financial', 'Communication Art')



lbch=tkinter.Label(frm,text="Club: ")
lbch.place(x=30,y=360)
lbch.config(font=("Times New Roman",16))


val_robot = tkinter.StringVar()
ch=tkinter.Checkbutton(frm,text="Robot",variable=val_robot,offvalue='',onvalue='Robot')
ch.place(x=150,y=360)
ch.config(font=("Times New Roman",16))

val_eng = tkinter.StringVar()
ch2=tkinter.Checkbutton(frm,text="English",variable=val_eng,onvalue='English',offvalue='')
ch2.place(x=280,y=360)
ch2.config(font=("Times New Roman",16))

val_startup = tkinter.StringVar()
ch3=tkinter.Checkbutton(frm,text="StartUp",variable=val_startup,onvalue='StartUp',offvalue='')
ch3.place(x=410,y=360)
ch3.config(font=("Times New Roman",16))

val_support = tkinter.StringVar()
ch4=tkinter.Checkbutton(frm,text="IT Support",variable=val_support,onvalue='IT Support',offvalue='')
ch4.place(x=530,y=360)
ch4.config(font=("Times New Roman",16))

val_iot = tkinter.StringVar()
ch5=tkinter.Checkbutton(frm,text="IoT",variable=val_iot,onvalue='IoT',offvalue='')
ch5.place(x=680,y=360)
ch5.config(font=("Times New Roman",16))

btnsave=tkinter.Button(frm,text="Save Infomation",width=20,command=save)
btnsave.place(x=150,y=450)
btnsave.config(font=("Times New Roman",16))

btncancel=tkinter.Button(frm,text="Cancel",width=20,command=quit)
btncancel.place(x=510,y=450)
btncancel.config(font=("Times New Roman",16))

lbB=tkinter.Label(frm,text="Birthdate: ")
lbB.place(x="410",y="10")
lbB.config(font=('Times New Roman',16))

cal = Calendar(frm, selectmode='day', date_pattern='y-mm-dd')
cal.place(x=430, y=50)
cal.config(font=('Times New Roman', 16))


frm.mainloop()