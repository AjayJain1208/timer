from tkinter import *
from tkinter import messagebox
from time import sleep

def start_timer(n):
    if variable.get()=='seconds':
        total_seconds = int(n)   
    else:
        total_seconds = int(n)*60
       
    sleep(total_seconds)
    messagebox.showinfo(title='Time ended', message="Time Up!")
    

root = Tk()
root.geometry("400x300")

Label(text="Timer",font=('Algerian',30), anchor=CENTER).place(relx=0.5, rely=0.1, anchor=CENTER )
Label(text="Set a timer: ").place(relx=0.1,rely=0.35)
# Label(text="min").place(relx=0.6,rely=0.35)

time_ = Entry(width=8)
time_.place(relx=0.38,rely=0.35)

option = ['seconds','minutes']
variable = StringVar()
variable.set(option[0])
# variable.set(option[0])
OptionMenu(root,variable,*option).place(relx=0.6,rely=0.33)

Button(text="Start timer", command=lambda:start_timer(time_.get())).place(relx=0.35,rely=0.5)

root.mainloop() 
