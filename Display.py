import mysql.connector as mysql
import tkinter
from tkinter import ttk
import tkinter.messagebox as Messagebox
import os
frm=tkinter.Tk()

con = mysql.connect(host="localhost",user="root",password="" , database="python_gui")
custor=con.cursor()
query = "select id, f_name, l_name, gender, tel_number from tbl_member"
custor.execute(query)

records = custor.fetchall()

frm.geometry("1000x450")
frm.title("Display Information")

def upData():
    index = myTree.selection()
    memID = myTree.item(index)["values"]
    if(type(memID)==list):
        file = open('info.txt','w')
        file.write(str(memID[0]))
        file.close()
        frm.destroy()
        os.system("python update.py")

def delData():

    result=Messagebox.askquestion(title='Confirm',  message='Do you want to delete',)
    if result:
        index = myTree.selection()
        memID=myTree.item(index)["values"]
        myTree.delete(index)
        delID=str(memID[0])
        query ="delete from tbl_member where id="+delID+""
      
        custor.execute(query)
        custor.execute("commit")

        custor.execute("Set @autoid:=0")
        custor.execute("UPDATE tbl_member set id=@autoid := (@autoid+1);")
        custor.execute("ALTER TABLE tbl_member AUTO_INCREMENT=1")
        custor.execute("commit")
        

myTree = ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings")
myTree.pack()

style=ttk.Style()
style.configure("Treeview.Heading",font =('Times New Roman',16))
style.configure("Treeview",font =('Times New Roman',14))

myTree.heading(1,text="ID",)
myTree.heading(2,text="Firstname",anchor='w')
myTree.heading(3,text="Lastname",anchor='w')
myTree.heading(4,text="Gender",)
myTree.heading(5,text="Tel",anchor='w')

myTree.column(1,width=100,anchor='center')
myTree.column(2,width=200,anchor='w')
myTree.column(3,width=200,anchor='w')
myTree.column(4,width=150,anchor='center')
myTree.column(5,width=150,anchor='w')

#loop data from database
val = [1,2,3,4,5]
global count
count=0


for a in records:
    myTree.insert(parent='',index='end', iid=count,text='',values=records[count])
    count+=1



btn_del=tkinter.Button(frm,text="Delete",width=15,command=delData)
btn_del.place(x=790,y=250)

btn_up=tkinter.Button(frm,text="Update",width=15,command=upData)
btn_up.place(x=650,y=250)
frm.mainloop()