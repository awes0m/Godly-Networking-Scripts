import socket

host= "tulpwctxavt1"
ip_addr="10.248.0.42"

#host to ip
def hostToip(*args):
    for data in args:
        ip=socket.gethostbyname(data)
        print(args[0],ip)
        print(type(ip))

#ip to host
def ipTohost(*args):
    for data in args:
        hostname=socket.gethostbyaddr(data)
        print(type(hostname[0]))
        print(args[0],hostname[0])

ipTohost(ip_addr)
hostToip(host)