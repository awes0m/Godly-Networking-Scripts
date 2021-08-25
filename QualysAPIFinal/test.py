from logic.Add_ip import add_ip

USERNAME = "wamsn_qa1"
PASSWORD = "WlqZwBKh7Fn72pUr"

with open("processedIp_list.txt",'r') as df:
    data=df.read()
                
# modulechooser=input("""Modules to Update:
#                                 b=Both VM and PC
#                                 vm= Only VM
#                                 pc=Only PC
                                
#                                 => """)
# enable_vm = 1 if modulechooser in ['b', 'vm'] else 0
# enable_pc = '1' if modulechooser in ['b', 'pc'] else '0'
print ("now requesting API...")
add_ip(USERNAME,PASSWORD,data)


