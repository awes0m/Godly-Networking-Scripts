import socket

host= "tulpwctxavt1"
ip_addr="10.248.0.42"

class NSLookup:
    def __init__(self):
        self.ip,
        self.hostname
    #host to ip
    def hostToip(hostname):
        return socket.gethostbyname(hostname)
        
            

    #ip to host
    def ipTohost(ip):
        hostName=socket.gethostbyaddr(ip)
        return hostName[0]

    print(ipTohost(ip_addr))
    print(hostToip(host))