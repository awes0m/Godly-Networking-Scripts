
from tkinter import messagebox
from tkinter import *
import os

from requests import NullHandler
from os.path import exists
from methods.apifunctions import ApiFunction

#-----------------------------Global Constants and Initializers---------------------------------#
USERNAME = "wamsn_qa1"
PASSWORD = "ruhn5rPWvsjGpJF"
endpoint_url ="https://qualysapi.qualys.com/api/2.0/fo/session/"
session_ID=None
uniqueid='1525419'



#-----------------------------------------UI-Logics-----------------------------------------------#

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
    # elif username.get().isEmpty() and password.get().isEmpty():
    #     messagebox.showinfo(
    #         title='Information',
    #         message='Username and Password not Submitted!'
    # )
    else:
        messagebox.showinfo(
        title='Information',
        message='Username and Password Submitted!'
    )
        confirm.config(state=DISABLED)
        reset_button.config(state=NORMAL)
        uniqueIdEntry.insert("Asset Group UniqueID")
        uniqueIdEntry.focus()

def reset():
    
    confirm.config(state=NORMAL)
    reset_button.config(state=DISABLED)

def update_Assets():
    USERNAME=username.get()
    PASSWORD=password.get()
    uniqueid=uniqueIdEntry.get()


    af=ApiFunction(USERNAME,PASSWORD,uniqueid),
    
    af.add_ip(),

    af.clear_asset_group(),
    af.update_Asset_group(),
    




#-----------------------------------------UI-----------------------------------------------#
window=Tk()
window.title("Som edition-Qualys Automater")
window.minsize(width=400,height=200)
Hero=Label(text="""
✩░▒▓▆▅▃▂▁Godly 𝐐𝐮𝐚𝐥𝐲𝐬 Automater▁▂▃▅▆▓▒░✩ 
==========================================
""")
#labels
Usernamelabel = Label(text="Username")
Passwordlabel=Label(text="Password")
WorkLabel1=Label(text="Enter Host data here--->                    ")
#Entries
username=Entry(width=30)
username.focus()
password=Entry(width=30)
uniqueIdEntry=Entry(width=30)
#buttons
confirm=Button(text="Submit/Lock",command=submitted,width= 20)
reset_button=Button(text="Reset",command=reset,width= 20)
reset_button.config(state=DISABLED)


OpenFile=Button(text="Open IP List",command=NullHandler)
Assetgroup_update=Button(text="Update Asset",command=NullHandler)


openfile=Button(text="Open file",command=open_file,width= 20)

#------------------------------Grid layout
#labels
Hero.grid(column=1,row=0,columnspan=3)
Usernamelabel.grid(column=1,row=1)
Passwordlabel.grid(column=1,row=2)
WorkLabel1.grid(column=1,row=4,columnspan=3)
#entries
username.grid(column=2,row=1)
password.grid(column=2,row=2)
#buttons
confirm.grid(column=3,row=2)
reset_button.grid(column=3,row=1)
uniqueIdEntry.grid(column=2,row =5)
Assetgroup_update.grid(column=3,row=5)
openfile.grid(column=3,row=4)


window.mainloop()
#-----------------------------------------xx----------------------------------------------------
