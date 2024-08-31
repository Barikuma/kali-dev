from netmiko import ConnectHandler
from getpass import getpass


hosts = ["192.168.0.105", "192.168.0.106"]

for host in hosts:
    device = {
                'host': host,
                'device_type': 'cisco_ios',
                'username': "admin",
                'password': "cisco"
            }

    with ConnectHandler(**device) as netdev:
        output = netdev.send_command("show ip interface brief")

    print(f"\nHost {host}\n{output}")


print("END...##")
