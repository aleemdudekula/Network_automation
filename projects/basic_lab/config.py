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

output = net_connect.send_config_from_file("cmds.txt")
#output = net_connect.send_command("show ip interface brief")
print(output)
