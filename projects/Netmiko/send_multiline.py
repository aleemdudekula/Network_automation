from netmiko import ConnectHandler
device_details = {
    "device_type": "cisco_ios",
    "host" : "192.168.79.32",
    "username": "aleem",
    "password" : "Condor@8",
    "secret" : "cisco123"
}
net_connect = ConnectHandler(**device_details)
net_connect.enable()

output = net_connect.send_multiline(["show ip interface brief"],
                                    ["show running-config"])
print(output)
# Please remove output before run above program 
output
(.network-aut) root@ubuntu:~/Network_automation/projects/basic_lab# python3 config.py
show ip interface brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            unassigned      YES NVRAM  administratively down down    
FastEthernet1/0            unassigned      YES NVRAM  administratively down down    
FastEthernet2/0            unassigned      YES NVRAM  administratively down down    
FastEthernet3/0            unassigned      YES NVRAM  administratively down down    
FastEthernet4/0            unassigned      YES NVRAM  administratively down down    
FastEthernet5/0            unassigned      YES NVRAM  administratively down down    
Ethernet6/0                192.168.1.1     YES manual up                    up      
Ethernet6/1                192.168.79.32   YES manual up                    up      
Ethernet6/2                unassigned      YES NVRAM  administratively down down    
Ethernet6/3                unassigned      YES NVRAM  administratively down down    
R2#
