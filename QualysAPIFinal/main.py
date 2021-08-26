
from models.InputDataProcessing import InputDataProcessor
from tkinter import messagebox
from tkinter import *
import os,datetime
import data.constant as const
import subprocess   

from os.path import exists

from logic.Add_ip import add_ip
from logic.ClearNUpdate_asset_group import *
from logic.Update_auth import *


#-----------------------------Global Constants and Initializers---------------------------------#
USERNAME = const.USERNAME
PASSWORD = const.PASSWORD
endpoint_url ="https://qualysapi.qualys.com/api/2.0/fo/session/"


file_id=const.FILE_ID
#-----------------------------------FilePaths---------------------------#

RawData_path=os.path.join(os.path.dirname('QualysAPIFinal\RawData\dataList.csv'),'dataList.csv')

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
                a =Open File to enter data
                b =process data
                c =Add IPs
                d =Update asset Group
                e =Update Authe Records
                l =Open Logs
                x =exit
                
                =>""")
    if choice in {'a', 'b', 'c', 'd', 'e','x','l'}:
        
        if choice == 'a':
            t=input("PLEASE SAVE FILE AFTER ENTERING DATA-------- Enter to confirm")
            open_file(RawData_path)

        elif choice == 'b':
            data=InputDataProcessor(RawData_path)
            logcheck=input ("Do you Want to check errorlog -Y/n =>  ")
            if logcheck in ['Y','y']:
                os.startfile("QualysAPIFinal\Logs\Ip_hosterrors\ipconvert_errorlog.csv")

            elif logcheck not in ['N', 'n']:
                print("Invalid Entry")

        elif choice == 'c':
            chooser_c()
        elif choice == 'd':
            chooser_d()
        elif choice == 'e':
            with open("QualysAPIFinal/data/dataA.txt",'r') as dA:
                dataA=dA.read()
            with open("QualysAPIFinal/data/dataB.txt",'r') as dB:
                dataB=dB.read()


            oschooser =input("""Modules to Update:
                                w = Windows
                                u = Unix
                                
                                ==>""")
            uniqueid=input("Enter Uniquie ID of Authentication record  ")

            if oschooser== 'w':
                auth_add_windows(USERNAME,PASSWORD,uniqueid,dataA,file_id=f'{file_id}_A')
                auth_add_windows(USERNAME,PASSWORD,uniqueid,dataB,file_id=f'{file_id}_B')

            elif oschooser== 'u':
                add_auth_unix(USERNAME,PASSWORD,uniqueid,dataA,file_id=f'{file_id}_A')
                add_auth_unix(USERNAME,PASSWORD,uniqueid,dataB,file_id=f'{file_id}_B')


        elif choice == 'l':
            subprocess.Popen(r'explorer /select,"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\Logs\ApiLogs"')
            
        if choice=='x':
            exit()

    else:
        print("Enter Valid Input please")

    print("Function completed !!")
    x=input("Run Again....? Y/n  - ")
    if x in ['Y','y']:
        chooser()
    elif x in ['N','n']:
        exit()   

def chooser_d():
    with open("QualysAPIFinal/data/dataA.txt",'r') as dA:
        dataA=dA.read()
    with open("QualysAPIFinal/data/dataB.txt",'r') as dB:
        dataB=dB.read()


    uniqueid=input("Enter Uniquie ID of asset group")
    wheel = ('-', '/', '|', '\\')

    print("assets group cleared now updating new ips")
    clear_asset_group(USERNAME,PASSWORD,uniqueid,file_id=f'{file_id}_A')
    print("assets group cleared now updating new ips")
    print(wheel)
    update_Asset_group(USERNAME,PASSWORD,uniqueid,dataA,file_id=f'{file_id}_A')
    update_Asset_group(USERNAME,PASSWORD,uniqueid,dataB,file_id=f'{file_id}_B')

def chooser_c():
    with open("QualysAPIFinal/data/dataA.txt",'r') as dA:
        dataA=dA.read()
    with open("QualysAPIFinal/data/dataB.txt",'r') as dB:
        dataB=dB.read()
    modulechooser=input("""Modules to Update:
                                b = Both VM and PC
                                vm = Only VM
                                pc = Only PC
                                
                                ==> """)
    enable_vm = '1' if modulechooser in ['b', 'vm'] else '0'
    enable_pc = '1' if modulechooser in ['b', 'pc'] else '0'

    add_ip(USERNAME,PASSWORD,dataA,f'{file_id}_A',enable_vm,enable_pc)
    print("set_a")
    add_ip(USERNAME,PASSWORD,dataB,f'{file_id}_B',enable_vm,enable_pc)
    print("ips added to host asset")   
#================================== ===

print("Qualys Asset updater")
chooser()
        
        
        
