
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
    messagebox.showinfo(
        title='Information',
        message='Username and Password Submitted!'
    )
    confirm.config(state=DISABLED)
    reset_button.config(state=NORMAL)
def reset():
    if username.get().isEmpty():
        messagebox.showinfo(
            title='Information',
            message='Username and Password Submitted!'
    )
    confirm.config(state=NORMAL)
    reset_button.config(state=DISABLED)

# af=ApiFunction(USERNAME,PASSWORD,uniqueid),

# af.clear_asset_group(),
# af.update_Asset_group(),




#-----------------------------------------UI-----------------------------------------------#
window=Tk()
window.title("Api upload")
window.minsize(width=400,height=200)
#Entries
Usernamelabel = Label(text="Username")
Passwordlabel=Label(text="Password")
username=Entry(width=30)
username.focus()
password=Entry(width=30)
uniqueid=Entry(width=30)
confirm=Button(text="Submit and Lock",command=submitted)
reset_button=Button(text="Submit and Lock",command=reset)
reset_button.config(state=DISABLED)


OpenFile=Button(text="Open IP List",command=NullHandler)
Assetgroup_update=Button(text="Update Asset",command=NullHandler)


openfile=Button(command=open_file)
openfile.config(text="open file")

#------------------------------Grid layout
Usernamelabel.grid(column=1,row=1)
Passwordlabel.grid(column=1,row=2)
username.grid(column=2,row=1)
password.grid(column=2,row=2)


Assetgroup_update.grid(column=2,row=4)
openfile.grid(column=3,row=4)


window.mainloop()
#-----------------------------------------xx----------------------------------------------------
