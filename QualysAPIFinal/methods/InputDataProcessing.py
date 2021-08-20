import os
import socket

#globalConstants
data=[]
ipData=[]

      
def hosttoip(hostdata):
    global ipData
    if os.path.exists(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\methods\Logs\ipconvert_errorlog.csv"):
        os.remove(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\methods\Logs\ipconvert_errorlog.csv")
    else:
        with open(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\methods\Logs\ipconvert_errorlog.csv", 'w+')as errfile:
            for i in hostdata:
            
                try:
                    print(f"Processing ip {str(socket.gethostbyname_ex(i)[2])}")
                    ipData.append(str(socket.gethostbyname_ex(i)[2][0]))
                except Exception as err:
                    print(f"Error Processing {i} , Check error log for more(ipconvert_errorlog.csv)")
                    errfile.write(f"{i},{err} \n")
        print ("All (possible) Hosts converted to ip")


def IPrangeConverter(iplist):
    # ipSplit=[i.split(".") for i in iplist]
    for ip in sorted(iplist, key = lambda ip: [int(ip) for ip in ip.split(".")] ):
            print(ip)


with open(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\test.txt", 'rb') as f:
    data=[i.decode().split('.')[0].upper() for i in f] 
hosttoip(data)
IPrangeConverter(ipData)