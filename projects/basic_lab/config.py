from netmiko import ConnectHandler
device_details = {
    "device_type": "cisco_ios",
    "host" : "192.168.79.10",
    "username": "aleem",
    "password" : "Condor@8",
    "secret" : "cisco123"
}
net_connect = ConnectHandler(**device_details)
net_connect.enable()

output = net_connect.send_command("show ip int brief")
print(output)

net_connect.disconnect()

