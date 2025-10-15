from netmiko import ConnectHandler
import json
from backup_devices import backup

with open('../devicesA.json') as f:
    devices = json.load(f)


commands = ['ip access-list standard MGMT_ACCESS',
            'permit 10.0.0.192 0.0.0.15',
            'permit 10.0.1.192 0.0.0.15',
            'deny any',
            'exit',
            'line vty 0 4',
            'access-class MGMT_ACCESS in'
            ]

for device in devices.items():
    ip = {
        'device_type': 'cisco_ios',
        'host': device[1]['mgmt_ip'],
        'username': 'admin',
        'password': 'cisco',
        'secret': 'cisco',
        'port': 22,
        'verbose': True
    }
    connection = ConnectHandler(**ip)
    print(f'Entering enable mode...')
    connection.enable()
    connection.send_config_set(commands)
    backup(connection)

    print('Closing connection...')
    connection.disconnect()
    print('#' * 30)
