
import subprocess

# Takes an Ip adress or Hostname 
# and returns an string arrray [HOSTNAME,IP_adress]
#to get host Nslookup(data)[0]
#to get IP_adrr Nslookup(data)[1]
        
def NSLookup(Host_ip='localhost'):
    process = subprocess.Popen(["nslookup", f"{Host_ip}"], stdout=subprocess.PIPE)

    output = process.communicate()[0].decode().split('\n')

    host_arr = [data.replace('Name: ','') for data in output if 'Name' in data]
    ip_arr = [data.replace('Address: ','') for data in output if 'Address' in data]
    ip_arr.pop(0)
    return [str(host_arr[0]).strip(),str(ip_arr[0]).strip()]








# import socket

# # host to ip
# def hostToip(hostname="localhost"):
#     return socket.gethostbyname(hostname)

#  # ip to host

# def ipTohost(ip="127.0.0.0"):
#     hostName = socket.gethostbyaddr(ip)
#     return hostName[0]





