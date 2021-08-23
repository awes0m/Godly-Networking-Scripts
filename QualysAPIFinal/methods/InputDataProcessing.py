import os
import socket


def hosttoip(hostdata):
    ipData = []
    if os.path.exists(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\methods\Logs\ipconvert_errorlog.csv"):
        os.remove(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\methods\Logs\ipconvert_errorlog.csv")
        f = open(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\methods\Logs\ipconvert_errorlog.csv", 'w+')
        f.close()

    with open(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\QualysAPIFinal\methods\Logs\ipconvert_errorlog.csv", 'w+')as errfile:
        for i in hostdata:

            try:
                print(f"Processing ip {str(socket.gethostbyname_ex(i)[2])}")
                ipData.append(str(socket.gethostbyname_ex(i)[2][0]))
            except Exception as err:
                print(
                    f"Error Processing {i} , Check error log for more(ipconvert_errorlog.csv)")
                errfile.write(f"{i},{err} \n")
        print("All (possible) Hosts converted to ip")
    return ipData


def IPSorter(iplist):
    return [
        ip
        for ip in sorted(
            iplist, key=lambda ip: [int(ip) for ip in ip.split(".")]
        )
    ]


def listToString(s): 
    return "".join(str(each) for each in s)
def IpToQualysdata(sortedIPData=[]):
    for _ in range(len(sortedIPData)-1):
        ip = sortedIPData[_]
        IPnumber = int(listToString([int(ip) for ip in ip.split(".")]))
        nxtip=sortedIPData[_+1]
        nxtIPnumber = int(listToString([int(nxtip) for nxtip in nxtip.split(".")]))
        
        
        
        
        
        
        
        
        
        
        


def filetoHostList(file=r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\test.txt"):
    with open(file, 'rb') as f:
        return [i.decode().split('.')[0].upper() for i in f]


filepath = r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\ip_list.csv"
data = filetoHostList()
ipData = hosttoip(data)
sortedIPData = IPSorter(ipData)
IpToQualysdata(sortedIPData)
