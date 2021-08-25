#-----------------------------------------UI-Logics-----------------------------------------------#
from tkinter import messagebox
from tkinter import *
import os
from requests import NullHandler
from os.path import exists

from screens.Update_asset_group import assetUpdateUI


def open_file():
    filename="ips_list.csv"
    if not exists("ips_list.csv"):
        f= open(f"{filename}","w+")
        f.close
    os.startfile(f'{filename}')
    
    
def submitted():
    if username.get()=="" or password.get()=="":
        messagebox.showinfo(
            title='Information',
            message='Username/Password not Submitted!'
    )
    else:
        messagebox.showinfo(
        title='Information',
        message='Username and Password Submitted!'
    )
        confirm.config(state=DISABLED)
        reset_button.config(state=NORMAL)

def reset():
    
    confirm.config(state=NORMAL)
    reset_button.config(state=DISABLED)
    
#-----------------------------------------UI-----------------------------------------------#
window=Tk()
window.title("Som edition-Qualys Automater")
window.minsize(width=400,height=200)
Hero=Label(text="""
✩░▒▓▆▅▃▂▁Godly 𝐐𝐮𝐚𝐥𝐲𝐬 Automater▁▂▃▅▆▓▒░✩ 
==========================================
""")
#labels
Usernamelabel = Label(window,text="Username",anchor='e')
Passwordlabel=Label(window,text="Password",anchor='e')
WorkLabel1=Label(window,text="Enter Data here(*SAVE after completion)->",anchor='e')
#Entries
username=Entry(window,width=30)
username.focus()
password=Entry(window,width=30)
#buttons
confirm=Button(window,text="Submit/Lock",command=submitted,width= 20)
reset_button=Button(window,text="Reset",command=reset,width= 20)
reset_button.config(state=DISABLED)


OpenFile=Button(window,text="Open IP List",command=open_file)
Assetgroup_update=Button(window,text="Update Asset",command=assetUpdateUI)


openfile=Button(window,text="Open file",command=open_file,width= 20)

#------------------------------Grid layout
#labels
Hero.grid(column=1,row=0,columnspan=3)
Usernamelabel.grid(column=1,row=1)
Passwordlabel.grid(column=1,row=2)
WorkLabel1.grid(column=1,row=4,columnspan=2)
#entries
username.grid(column=2,row=1)
password.grid(column=2,row=2)
#buttons
confirm.grid(column=3,row=2)
reset_button.grid(column=3,row=1)

Assetgroup_update.grid(column=3,row=5)
openfile.grid(column=3,row=4)


window.mainloop()