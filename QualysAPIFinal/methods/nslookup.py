import subprocess

process = subprocess.Popen(["nslookup", "www.google.com"], stdout=subprocess.PIPE)
output = process.communicate()[0].split('\n')

ip_arr = []
for data in output:
    if 'Address' in data:
        ip_arr.append(data.replace('Address: ',''))
ip_arr.pop(0)

print ip_arr

# import socket

# # host to ip
# def hostToip(hostname="localhost"):
#     return socket.gethostbyname(hostname)

 # ip to host

def ipTohost(ip="127.0.0.0"):
    hostName = socket.gethostbyaddr(ip)
    return hostName[0]
