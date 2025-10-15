from netmiko import ConnectHandler
import json
import ipaddress

with open('../devicesA.json') as file:
    devices_info = json.load(file)


for device in devices_info.values():
    # for interface, value in device['interfaces'].items():
    #     print(interface)
    #     print(value[:-3])
    #     mask = value[-2:]
    #     print(mask)
    #     net = ipaddress.IPv4Network(f"0.0.0.0/{mask}")
    #     print(net.netmask)

    ip = {'device_type': 'cisco_ios',
                                 'host': device['mgmt_ip'],
                                 'username': 'admin',
                                 'password': 'cisco',
                                 'port':22,
                                 'secret': 'cisco',
                                 'verbose': True
                                 }
    print(ip)
    connection = ConnectHandler(**ip)
    print('Entering enable mode...')
    connection.enable()
    commands = []
    for interface, value in device['interfaces'].items():
        mask = value[-2:]
        net = ipaddress.IPv4Network(f"0.0.0.0/{mask}")

        commands.append(f"int {interface}")
        commands.append(f"ip address {value[:-3]} {net.netmask}")

    connection.send_config_set(commands)

    connection.disconnect()



