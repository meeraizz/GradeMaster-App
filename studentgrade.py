from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Grade Master")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')
        self.root.focus_force()

        #===title====
        title=Label(self.root,text="Add Student Result",font=("times new roman",20,"bold"),bg="pink",fg="#262626").place(x=10,y=15,width=1260,height=50)

        #====variables====
        self.var_roll=StringVar
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]


        #===widgets===
        lbl_select = Label(self.root, text="Select Student", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks_obtained = Label(self.root, text="Marks Obtained", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks", font=("times new roman", 20, "bold"), bg="white").place(x=50, y=340)



        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("times new roman", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")





















if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()