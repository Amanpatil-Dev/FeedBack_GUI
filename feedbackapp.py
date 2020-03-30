

    


    


#CREATING A ROOT WINDOW
from tkinter import *
import tkinter as tk
from tkinter import Text
root=Tk()
root.title("FeedBack Form")
root.geometry("600x500")
root.configure(background="light blue")



#IMAGE

logo=tk.PhotoImage(file="C:\\Users\\LENOVO\\Documents\\fedb.gif")
explanation='''This is a feedback Form
Tell About The Session :-
Poor , Average , Good , Excellent'''


#FUNCTION THAT WILL STORE THE VALUES
def submit():
   print("stored")
   with open("record.txt","a") as f:
       f.write(f"{A.get(),B.get(),C.get()}\n")
       A.set(""), B.set(""), C.set("")
       top=Toplevel()
       top.title("Done")
       top.geometry("200x100")
       Label(top,text="Successfully Stored").grid(row=2,column=3)
       b=Button(top,text="Close",command=top.destroy)
       b.grid(column=3,padx=70)


#ADDRESSING WHERE TO PUT IMAGE
w1=Label(root,image=logo).grid(row=0,column=0)#.pack(side="left")
w2=Label(root,text=explanation,fg="blue").grid(row=0,column=1)#.pack(side="right")
#w2=tk.Label(root,justify=tk.CENTER,padx=10,text=explanation).pack(side="right")
#w1=tk.Label(root,compound=tk.CENTER,image=logo).pack(side="left")





#CREATING LABLES
L1=Label(root,padx=10,text="UserName").grid(row=2,column=0,pady=10)
L2=Label(root,padx=10,text="E-Mail ID").grid(row=3,column=0,pady=30)
L3=Label(root,padx=10,text="FeedBack").grid(row=4,column=0,pady=50)


#DECLARING THE VARIABLE TYPE
A=StringVar()
B=StringVar()
C=StringVar()


#MAKING THE ENTRY BOXES
E1=tk.Entry(root,width="40",textvariable=A).grid(row=2,column=1)
E2=tk.Entry(root,width="40",textvariable=B).grid(row=3,column=1)
E3=tk.Entry(root,width="40",textvariable=C).grid(row=4,column=1,ipady=20)#.pack(ipady=4)


#MAKING BUTTONS


b1=Button(root,text="Submit",command=submit).grid(row=5,column=1,padx=90)

root.mainloop()



    
