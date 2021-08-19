import socket

# host to ip
def hostToip(hostname="localhost"):
    return socket.gethostbyname(hostname)

 # ip to host

def ipTohost(ip="127.0.0.0"):
    hostName = socket.gethostbyaddr(ip)
    return hostName[0]
