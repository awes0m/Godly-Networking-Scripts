

from nslookup import hostToip
import os
import socket



# host to ip

data=[]
k=0
with open(r"C:\Users\ssubhra\Desktop\Git repositories\Godly-Networking-Scripts\ip_list.txt", 'rb') as f:
    data=[i.decode().split('.')[0].upper() for i in f]        
f.close

for i in data:
    print(hostToip(i))