import json

from debian.debtags import output
from netmiko import ConnectHandler
from datetime import datetime
import time


now = datetime.now()
year = now.year
month = now.month
day = now.day

with open('../devices.json') as file:
    device_info = json.load(file)

for device in device_info.values():
    ip = {'device_type': 'cisco_ios',
          'host': device['mgmt_ip'],
          'username': 'admin',
          'password': 'cisco',
          'port': 22,
          'secret': 'cisco',
          'verbose': True
          }

    connection = ConnectHandler(**ip)

    print('Entering enable mode...')
    connection.enable()
    connection.save_config()
    output = connection.send_command('sh run')
    prompt = connection.find_prompt()
    hostname = prompt[0:-1]

    filename = f'../backups/{hostname}_{year}-{month}-{day}_backup.txt'

    with open(filename, 'w') as f:
        f.write(filename)

    print('Closing connection ')
    connection.disconnect()
    print('#' * 30)
