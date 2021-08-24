
from tkinter import messagebox
from tkinter import *
import os
from requests import NullHandler
from os.path import exists

from logic.Add_ip import add_ip
from logic.ClearNUpdate_asset_group import *
from logic.Update_auth import *

from screens.Update_asset_group import assetUpdateUI

#-----------------------------Global Constants and Initializers---------------------------------#
USERNAME = "wamsn_qa1"
PASSWORD = "WlqZwBKh7Fn72pUr"
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
    else:
        messagebox.showinfo(
        title='Information',
        message='Username and Password Submitted!'
    )
        confirm.config(state=DISABLED)
        reset_button.config(state=NORMAL)
        uidAssetgroup.insert("Asset Group UniqueID")
        uidAssetgroup.focus()

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
Usernamelabel = Label(text="Username")
Passwordlabel=Label(text="Password")
WorkLabel1=Label(text="Enter Host data here--->                    ")
#Entries
username=Entry(width=30)
username.focus()
password=Entry(width=30)
uidAssetgroup=Entry(width=30)
uidAuthentication=Entry(width=30)
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
uidAssetgroup.grid(column=2,row =5)
Assetgroup_update.grid(column=3,row=5)
openfile.grid(column=3,row=4)


window.mainloop()
#-----------------------------------------xx----------------------------------------------------
