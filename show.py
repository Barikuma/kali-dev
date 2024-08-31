from netmiko import ConnectHandler
from getpass import getpass

username = input("Username: ")
password = getpass()

hosts = ["S1", "S2"]

for host in hosts:
    device = {
                'host': host,
                'device_type': 'cisco_ios',
                'username': username,
                'password': password
            }

    with ConnectHandler(**device) as netdev:
        output = netdev.send_command("show ip interface brief")

    print("\nHost {}\n{}".format(host, output))
