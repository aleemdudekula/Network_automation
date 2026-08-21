#import netmiko and ConnectHandler library 
from netmiko import ConnectHandler
#Device-information
device_details = {
    "device_type": "cisco_ios",
    "host" : "192.168.79.32",
    "username": "aleem",
    "password" : "Condor@8",
    "secret" : "cisco123"
}
#connection established through 'SSH'
net_connect = ConnectHandler(**device_details)
net_connect.enable()

output = net_connect.send_command("show ip interface brief")
print(output)
