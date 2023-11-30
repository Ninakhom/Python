import tkinter
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
con=mysql.connect(host="localhost",user="root",password="",database="python_gui")
custor=con.cursor()

frm=tkinter.Tk()
frm.geometry("550x550")
frm.title("Register From")


varGender=tkinter.IntVar()
varGender.set(1)

def insert():
    f_name=txt_first.get()
    l_name=txt_last.get()
    gender=varGender.get()
    tel_number=txt_tel.get()
    username=txt_pass.get()
    passwd=txt_pass.get()
    if (txt_pass.get() != txt_con.get()):
       Messagebox.showinfo("insert status","password not same")
       txt_con.delete(0,'end')


    else:
        query = "INSERT INTO tbl_member (f_name, l_name, gender, tel_number, username, passwd) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (f_name, l_name, gender, tel_number, username, passwd)
        custor.execute(query,values)
        custor.execute("commit")
        txt_first.delete(0,'end')
        txt_last.delete(0,'end')
        varGender.set(1)
        txt_tel.delete(0,'end')
        txt_user.delete(0,'end')
        txt_pass.delete(0,'end')
        txt_con.delete(0,'end')

lb1=tkinter.Label(frm,text="Firstname :")
lb1.place(x=20,y=30)
lb1.config(font=("Times New Roman",15))

txt_first=tkinter.Entry(frm)
txt_first.place(x=130,y=30)
txt_first.config(font=('Times New Roman',15))


lb2=tkinter.Label(frm,text="Lastname :")
lb2.place(x=20,y=70)
lb2.config(font=("Times New Roman",15))

txt_last=tkinter.Entry(frm)
txt_last.place(x=130,y=70)
txt_last.config(font=('Times New Roman',15))

lb3=tkinter.Label(frm,text="Gender :")
lb3.place(x=20,y=110)
lb3.config(font=("Times New Roman",15))

rd1=tkinter.Radiobutton(frm,text="Male",variable=varGender,value=1)
rd1.place(x=130,y=110)
rd1.config(font=("Times New Roman",15))

rd2=tkinter.Radiobutton(frm,text="Female",variable=varGender,value=2)
rd2.place(x=220,y=110)
rd2.config(font=("Times New Roman",15))

lb4=tkinter.Label(frm,text="Tel :")
lb4.place(x=20,y=150)
lb4.config(font=("Times New Roman",15))

txt_tel=tkinter.Entry(frm)
txt_tel.place(x=130,y=150)
txt_tel.config(font=('Times New Roman',15))

lb5=tkinter.Label(frm,text="Username :")
lb5.place(x=20,y=190)
lb5.config(font=("Times New Roman",15))

txt_user=tkinter.Entry(frm)
txt_user.place(x=130,y=190)
txt_user.config(font=('Times New Roman',15))

lb6=tkinter.Label(frm,text="Password :")
lb6.place(x=20,y=230)
lb6.config(font=("Times New Roman",15))

pss=tkinter.StringVar()
txt_pass=tkinter.Entry(frm,show='*',)
txt_pass.place(x=130,y=230)
txt_pass.config(font=('Times New Roman',15))

lb7=tkinter.Label(frm,text="Confirm :")
lb7.place(x=20,y=280)
lb7.config(font=("Times New Roman",15))

txt_con=tkinter.Entry(frm,show='*',)
txt_con.place(x=130,y=280)
txt_con.config(font=('Times New Roman',15))

btnre=tkinter.Button(frm,text="Register",width=7,command=insert)
btnre.place(x=170,y=350)
btnre.config(font=('Time New Roman',15))

btnre=tkinter.Button(frm,text="Cancel",width=7,command=quit)
btnre.place(x=270,y=350)
btnre.config(font=('Time New Roman',15))


frm.mainloop()