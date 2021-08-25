
from models.InputDataProcessing import InputDataProcessor
from tkinter import messagebox
from tkinter import *
import os
from requests import NullHandler
from os.path import exists

from logic.Add_ip import add_ip
from logic.ClearNUpdate_asset_group import *
from logic.Update_auth import *


#-----------------------------Global Constants and Initializers---------------------------------#
USERNAME = "wamsn_qa1"
PASSWORD = "WlqZwBKh7Fn72pUr"
endpoint_url ="https://qualysapi.qualys.com/api/2.0/fo/session/"
session_ID=None
uniqueid='1525419'
data=[]

#-----------------------------------------UI-Logics-----------------------------------------------#

def open_file(filename):
    if not exists(filename):
        f= open(f"{filename}","w+")
        f.close
    os.startfile(f'{filename}')


#-----------------------------------------xx----------------------------------------------------


def chooser():
    global data
    choice= input("""Enter choice:
                a=Open File to enter data
                b=process data
                c=Add IPs
                d=Update asset Group
                e=Update Authe Records
                
                =>""")
    if choice in {'a', 'b', 'c', 'd', 'e'}:
        
        if choice == 'a':
            open_file("dataList.csv")

        elif choice == 'b':
            data=InputDataProcessor()
            logcheck=input ("Do you Want to check errorlog -Y/n =>0")
            if logcheck in ['Y','y']:
                os.startfile("QualysAPIFinal\models\Logs\ipconvert_errorlog.csv")

            elif logcheck not in ['N', 'n']:
                print("Invalid Entry")

        elif choice == 'c':
            with open("processedIp_list.txt",'r') as df:
                data=df.read()
                
            modulechooser=input("""Modules to Update:
                                b=Both VM and PC
                                vm= Only VM
                                pc=Only PC""")
            enable_vm = '1' if modulechooser in ['b', 'vm'] else '0'
            enable_pc = '1' if modulechooser in ['b', 'pc'] else '0'

            add_ip(USERNAME,PASSWORD,data,enable_vm,enable_pc)

        elif choice == 'd':
            with open("processedip_list.txt",'r') as df:
                data=df.read()
                
            uniqueid=input("Enter Uniquie ID of asset group")
            clear_asset_group(USERNAME,PASSWORD,uniqueid)
            update_Asset_group(USERNAME,PASSWORD,uniqueid,data)

        elif choice == 'e':
            with open("processedip_list.txt",'r') as df:
                data=df.read()
                
            oschooser =int (input("""Modules to Update:
                                w=Windows
                                u= Unix"""))
            uniqueid=int (input("Enter Uniquie ID of Authentication record"))

            if oschooser== 'w':
                auth_add_windows(USERNAME,PASSWORD,uniqueid,data)
            elif oschooser== 'u':
                add_auth_unix(USERNAME,PASSWORD,uniqueid,data)

    else:
        print("Enter Valid Input please")
    chooser()   
#================================== ===

print("Qualys Asset updater")
chooser()
        
        
        
