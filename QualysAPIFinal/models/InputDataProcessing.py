import os
import socket

#1.convert Hostnamestoipadresses
def hosttoip(hostdata): 
    #This takes a list of Hostname and converts to ipadresses
    #Also generates a error log file consisting of Hostnames that couldn't be found
    ipData = []
    if os.path.exists("QualysAPIFinal\models\Logs\ipconvert_errorlog.csv"):
        os.remove("QualysAPIFinal\models\Logs\ipconvert_errorlog.csv")
        f = open("QualysAPIFinal\models\Logs\ipconvert_errorlog.csv", 'w+')
        f.close()

    with open("QualysAPIFinal\models\Logs\ipconvert_errorlog.csv", 'w+')as errfile:
        for i in hostdata:

            try:
                print(f"Processing ip {i} -{str(socket.gethostbyname_ex(i)[2])}")
                ipData.append(str(socket.gethostbyname_ex(i)[2][0]))
            except Exception as err:
                print(
                    f"Error Processing {i} , Check error log for more(ipconvert_errorlog.csv)")
                errfile.write(f"{i},{err} \n")
        print("All (possible) Hosts converted to ip")
    return ipData

#2.sort the IP adresses in ascending Order
def IPSorter(iplist):
    #takes a list of [IPadresses] and returns a sorted list of IP adrersses
    return [
        ip
        for ip in sorted(
            iplist, key=lambda ip: [int(ip) for ip in ip.split(".")]
        )
    ]
    
#converts the single IP address into IPnumber(eg-10.20.30.22 => 10203022)
def IPnumber(ip):
    return int(listToString([int(ip) for ip in ip.split(".")]))

#for internal use converts a list to string
def listToString(s): 
    return "".join(str(each) for each in s)

#3.Group the converted and Sorted Ips into smaller lists and return the in Qualys acceptable Network ranges
def QualysFormatData(sortedIPData=[]):
    #takes a list of sorted IPS and returns a list of lists containing consequitive Ips clustered together
    vals=[IPnumber(n) for n in sortedIPData]
    rangedlist = []
    sublist = []
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
            k=vals.index(v)
            sublist.append(sortedIPData[k])
        else:
            run = [v]
            result.append(run)
            k=vals.index(v)
            sublist=[sortedIPData[k]]
            rangedlist.append(sublist)
        expect = v + 1
    # Converts the rangedlist(grouped ips) to Qualys readeable Ip ranges
    finaldata = []
    for each in rangedlist:
        if len(each)>1:
            finaldata.append(f"{each[0]}-{each[-1]}")
        else:
            finaldata.append(each[0])
    return finaldata
            
    
                
                        

def filetoHostList(file="test.txt"):
    with open(file, 'rb') as f:
        return [i.decode().split('.')[0].upper() for i in f]
#Main functionn that compiles all the other function(takes Hostnames => return s Qualys format data)
def InputDataProcessor():
    filepath = "dataList.csv"
    data = filetoHostList()
    ipData = hosttoip(data)
    sortedIPData = IPSorter(ipData)
    Qualysdata=QualysFormatData(sortedIPData)
    if os.path.exists("QualysAPIFinal\processedIp_list.txt"):
        os.remove("QualysAPIFinal\processedIp_list.txt")
        f = open("QualysAPIFinal\processedIp_list.txt", 'w+')
        f.close()

    with open('processedIp_list.txt','a') as of:
        for i in Qualysdata:
            of.write(f'{i},') 
            
    os.startfile('processedIp_list.txt')        
    return Qualysdata
