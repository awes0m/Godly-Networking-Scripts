import
import os


def NSLookup(Host_ip='127.0.0.1'):
    process = subprocess.Popen(["nslookup", f"{Host_ip}"], stdout=subprocess.PIPE)
    output= process.communicate()[0].decode().split('\n')
    host_arr = output[0][7:].strip()
    ip_arr = output[1][8:].strip()
    
    return [host_arr, ip_arr]


with open('hostlist.txt','r') as f:
    hostnames = f.read().splitlines()


nslookup_list = [NSLookup (host) for host in hostnames]
print(nslookup_list)

with open ('results.csv','w') as f:
    for host in nslookup_list:
        f.write(f'{host[0]},{host[1]}\n')

     
    

    