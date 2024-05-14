from tkinter import *
from PIL import Image, ImageTk    #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class DetailsClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #=====title======
        title=Label(self.root,text="Manage Student Details", font=("times new roman",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=45)

        #=====variables====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()

        #=====widgets======
        #=======column 1=========
        lbl_roll=Label(self.root,text="Roll No.", font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)                     
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
           
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=220,width=150)
        
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=220)
        txt_city=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=380,y=220,width=150)
        
        lbl_pin=Label(self.root,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=220)
        txt_pin=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=560,y=220,width=120)

        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=220)
        
        #====entry fields====
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_roll.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200,)
        self.txt_gender.current(0)

       #=======column 2=========
        lbl_dob=Label(self.root,text="D.O.B", font=("goudy old style",15,"bold"),bg="white").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=100)                     
        lbl_admission=Label(self.root,text="Admission",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=360,y=180)

        #====entry fields 2====
        self.course_list=[]
        #function_call to update the list
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=100,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=480,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=(" "),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200,)
        self.txt_course.set("Empty")
        
        #====text address=====
        self.txt_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_address.place(x=150,y=260,width=540,height=100)

        #=====buttons=======
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="blue")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="green")
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="red")
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="grey")
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #=======search panel=====
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        #=====content========
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address").xscroll)

        scrollx.pack(side=BOTTOM,fill=x)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]="headings"
        self.CourseTable.heading("roll",width=100)
        self.CourseTable.heading("name",width=100)
        self.CourseTable.heading("email",width=100)
        self.CourseTable.heading("gender",width=100)
        self.CourseTable.heading("dob",width=100)
        self.CourseTable.heading("contact",width=100)
        self.CourseTable.heading("admission",width=100)
        self.CourseTable.heading("course",width=100)
        self.CourseTable.heading("state",width=100)
        self.CourseTable.heading("city",width=100)
        self.CourseTable.heading("pin",width=100)
        self.CourseTable.heading("address",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

if __name__=="__main__":
    root=Tk()
    obj=DetailsClass(root)
    root.mainloop()        